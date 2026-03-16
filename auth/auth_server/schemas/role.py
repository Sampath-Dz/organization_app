from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str

class RoleRead(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}
