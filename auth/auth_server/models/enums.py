from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"

class TypeEnum(str, Enum):
    admin = "admin"
    user = "user"
    viewer = "viewer"
