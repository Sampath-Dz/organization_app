from enum import Enum

class ResourceType(str, Enum):
    ORGANIZATION = "organization"
    TEAM = "team"
    MEMBER = "member"
