
from pydantic import BaseModel, ConfigDict


class RoleCreate(BaseModel):
    name: str


class RoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class RoleListResponse(BaseModel):
    roles: list[RoleResponse]
    total: int
