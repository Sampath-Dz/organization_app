from pydantic import BaseModel

class TypeCreate(BaseModel):
    name: str

class TypeRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
