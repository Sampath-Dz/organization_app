from pydantic import BaseModel, ConfigDict
from typing import Optional


class TypeCreate(BaseModel):
    name: str


class TypeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class TypeListResponse(BaseModel):
    types: list[TypeResponse]
    total: int
