import enum
from http import HTTPStatus

class Err(enum.Enum):
    OC0001 = ["Wrong arguments: %s"]
    OC0002 = ["Method not allowed"]
    OC0003 = ["%s %s not found"]
    OC0004 = ["Not found"]
    OC0005 = ["Forbidden"]
    OC0006 = ["Unauthorized"]
    OC0007 = ["%s already exists"]
    OC0008 = ["Invalid token"]
    OC0009 = ["Authorization required"]
    OC0010 = ["Database error: %s"]
    OC0011 = ["Organization with id %s not found"]
    OC0012 = ["Team with id %s not found"]
    OC0013 = ["Member with id %s not found"]
    OC0014 = ["%s with id %s not found"]
    OC0020 = ["Validation error: %s"]
    OC0021 = ["%s is required"]

class CoreException(Exception):
    http_status: int = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, error: Err = None, params: list = None, detail: str = None):
        self.error = error
        self.params = params or []

        if detail:
            self.message = detail
        elif error:
            self.message = error.value[0] % tuple(self.params) if self.params else error.value[0]
        else:
            self.message = "Internal server error"

        self.error_code = error.name if error else "UNKNOWN"
        super().__init__(self.message)

    def to_dict(self):
        return {
            "error_code": self.error_code,
            "message": self.message,
        }

class NotFoundException(CoreException):
    http_status = HTTPStatus.NOT_FOUND

class AlreadyExistsException(CoreException):
    http_status = HTTPStatus.CONFLICT

class BadRequestException(CoreException):
    http_status = HTTPStatus.BAD_REQUEST

class UnauthorizedException(CoreException):
    http_status = HTTPStatus.UNAUTHORIZED

class ForbiddenException(CoreException):
    http_status = HTTPStatus.FORBIDDEN

class ConflictException(CoreException):
    http_status = HTTPStatus.CONFLICT

class WrongArgumentsException(CoreException):
    http_status = HTTPStatus.BAD_REQUEST

class InvalidTokenException(CoreException):
    http_status = HTTPStatus.UNAUTHORIZED
    def __init__(self, detail: str = None):
        super().__init__(error=Err.OC0008, detail=detail)