from pydantic import BaseModel

class TeamCreate(BaseModel):
    name: str
    organization_id: int

class TeamRead(BaseModel):
    id: int
    name: str
    organization_id: int
    
    class Config:
        orm_mode = True

