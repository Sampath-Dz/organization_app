from pydantic import BaseModel

<<<<<<< HEAD
class TeamCreate(BaseModel):
    name: str
    organization_id: int

class TeamRead(BaseModel):
    id: int
    name: str
    organization_id: int
    class Config:
        orm_mode = True
=======

class TeamCreate(BaseModel):

    name:str
    organization_id:int
>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
