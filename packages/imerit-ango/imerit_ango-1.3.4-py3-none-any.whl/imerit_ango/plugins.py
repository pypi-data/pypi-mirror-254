from dotenv import load_dotenv
import os
import time
import boto3
import queue
import logging
import datetime
import requests
import socketio
from io import BytesIO
from typing import Callable, Tuple
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Header, HTTPException, Depends
from mangum import Mangum

from imerit_ango.plugin_logger import PluginLogger
from imerit_ango.sdk import SDK
from typing import Dict, Any

try:
    import asyncio
except ImportError:
    import trollius as asyncio

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

CONNECTOR = os.environ.get('CONNECTOR', 'WS').upper()
PORT = int(os.environ.get('PORT', '8080'))


class Plugin(socketio.ClientNamespace):

    def __init__(self, id: str, secret: str, callback: Callable):
        super().__init__('/plugin')
        self.id = id
        self.secret = secret
        self.logger = logging.getLogger("plugin")
        self.logger.setLevel(LOGLEVEL)
        self.callback = callback

        if CONNECTOR == "WS":
            self.scheduler = BackgroundScheduler()
            self.scheduler.add_job(self.heartbeat, 'interval', seconds=60)
            self.scheduler.start()
            self.loop = asyncio.get_event_loop()

    def _callback(self, data, sdk = None):
        try:
            return self.callback(**data)
        except Exception as e:
            self.logger.error(e)
            response = {
                "error": True,
                "session": data.get("session", "")
            }
            if CONNECTOR == "WS":
                self.emit('response', response)
            else:
                if sdk is not None:
                    sdk._plugin_response(response)
                else:
                    raise e

    def on_connect(self):
        self.heartbeat()
        self.logger.warning("Connected")

    def on_disconnect(self):
        self.logger.warning("Disconnected")
        _connect_ws(self, self.client.connection_url)

    def heartbeat(self):
        try:
            self.emit('heartbeat', {"id": self.id, "secret": self.secret})
        except Exception as e:
            self.logger.critical(e)
            os._exit(1)
        self.logger.info("Heartbeat at %s" % str(time.time()))

    def on_plugin(self, data):
        data["logger"] = self._get_logger(data)
        data["batches"] = data.get('tags', [])
        response = {
            "response": self._callback(data),
            "session": data.get("session", "")
        }
        if CONNECTOR is not "WS":
            return response
        if response.get("response", None) is not None:
            self.emit('response', response)

    def _get_logger(self, data):
        org_id = data.get("orgId", "")
        run_by = data.get("runBy", "")
        session = data.get("session", "")
        apikey = data.get("apiKey", "")
        logger = PluginLogger("logger", self.id, org_id, apikey, run_by, session, self, CONNECTOR, LOGLEVEL)
        return logger

    def start(self):
        asyncio.get_event_loop().run_forever()


class ExportResponse:
    def __init__(self, file: BytesIO, file_name: str = "export.json", storage_id: str = None, bucket: str = None):
        self.file = file
        self.file_name = file_name
        self.storage_id = storage_id
        self.bucket = bucket


class ExportPlugin(Plugin):

    def __init__(self, id: str, secret: str, callback: Callable[[str, dict], Tuple[str, BytesIO]],
                 host="https://imeritapi.ango.ai", version: str = "v2"):
        super().__init__(id, secret, callback)
        self.host = host
        self.version = version

    def on_plugin(self, data):
        """
        :param data: {project_id: str, assignees: List[str] = None, completed_at: List[datetime.datetime] = None,
               updated_at: List[datetime.datetime = None, tags: List[str] = None}
        :return:
        """
        completed_at = None
        updated_at = None
        project_id = data.get('projectId')
        logger = super()._get_logger(data)
        api_key = data.get('apiKey')
        include_key_points_only = data.get('includeKeyPointsOnly', None)
        sdk = SDK(api_key=api_key, host=self.host)

        if data.get("completed_at", None):
            completed_at = [datetime.datetime.fromisoformat(data.completed_at[0]),
                            datetime.datetime.fromisoformat(data.completed_at[1])]
        if data.get("updated_at", None):
            updated_at = [datetime.datetime.fromisoformat(data.updated_at[0]),
                          datetime.datetime.fromisoformat(data.updated_at[1])]

        try:
            (json_export, num_lines) = sdk.exportV3(project_id, batches=data.get('batches', None),
                                                    stage=data.get('stage', None), export_format="ndjson",
                                                    include_key_points_only=include_key_points_only)
            data["numTasks"] = num_lines
        except Exception as e:
            logger.error(f"Error calling sdk.export: {e}")
            return

        data["jsonExport"] = json_export
        data["logger"] = logger

        resp = self._callback(data, sdk)

        if resp.storage_id:
            storage = sdk.get_storages(resp.storage_id)
            s3 = boto3.client('s3', region_name=storage.get('region'), aws_access_key_id=storage.get("publicKey"),
                              aws_secret_access_key=storage.get("privateKey"))
            signed_url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': resp.bucket, 'Key': resp.file_name},
                ExpiresIn=3600
            )
            upload_url = s3.generate_presigned_url(
                'put_object',
                Params={'Bucket': resp.bucket, 'Key': resp.file_name},
                ExpiresIn=3600
            )
        else:
            file_name = project_id + '/exports/' + resp.file_name
            upload_url = sdk._get_upload_url(file_name)
            signed_url = sdk._get_signed_url(upload_url)

        try:
            upload_resp = requests.put(upload_url, data=resp.file.getvalue())
            upload_resp.raise_for_status()
        except requests.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
        else:
            response = {
                "export": True,
                "response": signed_url,
                "session": data.get("session", "")
            }
            if CONNECTOR == "WS":
                self.emit('response', response)
            else:
                sdk._plugin_response(response)

class ModelPlugin(Plugin):
    def __init__(self, id: str, secret: str, callback: Callable, host="https://imeritapi.ango.ai", concurrency=1):
        super().__init__(id, secret, callback)
        self.host = host
        self.concurrency = concurrency
        self.queue = queue.Queue()

    async def work(self):
        while True:
            data = self.queue.get()
            data["batches"] = data.get('tags', [])
            api_key = data.get('apiKey')
            task_id = data.get('taskId')
            sdk = SDK(api_key=api_key, host=self.host)
            answer = self._callback(data, sdk)
            sdk._annotate(task_id, answer)

    def on_plugin(self, data):
        workflow = data.get('workflow')
        if not workflow:
            return super().on_plugin(data)
        self.queue.put(data)

    def start(self):
        tasks = [self.work() for i in range(self.concurrency)]
        future = asyncio.gather(*tasks)
        self.loop.run_until_complete(future)


class FileExplorerPlugin(Plugin):
    def __init__(self, id: str, secret: str, callback: Callable):
        super().__init__(id, secret, callback)


class BatchModelPlugin(Plugin):
    def __init__(self, id: str, secret: str, callback: Callable):
        super().__init__(id, secret, callback)


class InputPlugin(Plugin):
    def __init__(self, id: str, secret: str, callback: Callable):
        super().__init__(id, secret, callback)


class MarkdownPlugin(Plugin):
    def __init__(self, id: str, secret: str, callback: Callable):
        super().__init__(id, secret, callback)


def connect_rest(plugin):
    import uvicorn
    app = FastAPI()

    # Dependency function
    def get_authorization_info(Secret: str = Header(None)):
        if Secret != plugin.secret:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return True

    @app.post("/plugin")
    def plugin_query(payload: Dict[Any, Any], auth=Depends(get_authorization_info)):
        response = plugin.on_plugin(payload)
        return response

    @app.get("/heartbeat")
    def heartbeat(auth=Depends(get_authorization_info)):
        return "ok"

    if CONNECTOR == "REST":
        uvicorn.run(app, host="0.0.0.0", port=PORT)
    elif CONNECTOR == "LAMBDA":
        handler = Mangum(app, lifespan="off")
    else:
        raise Exception("Expecting CONNECTOR Environment variable")


def _connect_ws(plugin, host):
    try:
        sio = socketio.Client(logger=logging.getLogger("plugin"), reconnection=False)
        sio.register_namespace(plugin)
        sio.connect(host, namespaces=["/plugin"], transports=["websocket"], wait=True)
    except Exception as e:
        logging.getLogger().critical(e)
        os._exit(1)


def run(plugin, host="https://plugin.imerit.ango.ai"):
    if CONNECTOR == "WS":
        _connect_ws(plugin, host)
        try:
            plugin.start()
        except (KeyboardInterrupt, SystemExit):
            logging.getLogger().warning("Plugin Stopped")
            os._exit(1)
    else:
        connect_rest(plugin)
