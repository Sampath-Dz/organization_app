from fastapi import HTTPException

class UserAlreadyExists(HTTPException):

    def __init__(self):

        super().__init__(

            status_code=400,

            detail="User already exists"
        )


class ResourceNotFound(HTTPException):

    def __init__(self):

        super().__init__(

            status_code=404,

            detail="Resource not found"
        )
