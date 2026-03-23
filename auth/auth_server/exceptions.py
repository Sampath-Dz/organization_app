
import enum
from http import HTTPStatus

class Err(enum.Enum):
    AUTH0001 = ["Wrong arguments: %s"]
    AUTH0002 = ["Method not allowed"]
    AUTH0003 = ["%s %s not found"]
    AUTH0004 = ["Not found"]
    AUTH0005 = ["Forbidden"]
    AUTH0006 = ["Unauthorized"]
    AUTH0007 = ["%s already exists"]
    AUTH0008 = ["Invalid token"]
    AUTH0009 = ["Authorization required"]
    AUTH0010 = ["Database error: %s"]
    AUTH0020 = ["Validation error: %s"]
    AUTH0021 = ["%s is required"]

class AuthException(Exception):
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

class NotFoundException(AuthException):
    http_status = HTTPStatus.NOT_FOUND

class AlreadyExistsException(AuthException):
    http_status = HTTPStatus.CONFLICT

class BadRequestException(AuthException):
    http_status = HTTPStatus.BAD_REQUEST

class UnauthorizedException(AuthException):
    http_status = HTTPStatus.UNAUTHORIZED

class ForbiddenException(AuthException):
    http_status = HTTPStatus.FORBIDDEN

class ConflictException(AuthException):
    http_status = HTTPStatus.CONFLICT

class WrongArgumentsException(AuthException):
    http_status = HTTPStatus.BAD_REQUEST
