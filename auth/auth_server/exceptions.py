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


class AppException(HTTPException):

    def __init__(self,status_code:int,message:str):

        super().__init__(status_code=status_code,detail=message)



from fastapi import HTTPException

if db.query(User).filter(User.mail==data.mail).first():
    raise HTTPException(status_code=400, detail="Email already exists")
