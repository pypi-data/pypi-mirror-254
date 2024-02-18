from enum import Enum

class Metrics(Enum):
    LabelStageGroups = 'LabelStageGroups'
    TimePerTask = 'TimePerTask'
    AnnotationStatus = 'AnnotationStatus'
    AnswerDistribution = 'AnswerDistribution'
    ConsensusRanges = 'ConsensusRanges'
    AssetSize = 'AssetSize'

class OrganizationRoles(Enum):
    Member = 'member'
    Admin = 'admin'

class ProjectRoles(Enum):
    Manager = 'Manager'
    Labeler = 'Labeler'
    Reviewer = 'Reviewer'
    Lead = 'Lead'
