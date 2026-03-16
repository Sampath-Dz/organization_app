from pydantic import BaseModel

class TypeCreate(BaseModel):
    name: str

class TypeRead(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}
