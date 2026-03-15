from pydantic import BaseModel

<<<<<<< HEAD
class MemberCreate(BaseModel):
    name: str
    team_id: int

class MemberRead(BaseModel):
    id: int
    name: str
    team_id: int
    class Config:
        orm_mode = True
=======

class MemberCreate(BaseModel):

    name:str
    team_id:int
>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
