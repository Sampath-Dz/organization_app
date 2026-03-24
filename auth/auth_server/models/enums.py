from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"

class TypeEnum(str, Enum):
    organization = "organization"
    team = "team"

class TokenType(Enum): 
    ACCESS  = 'access'
    REFRESH = 'refresh'