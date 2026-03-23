from pydantic import field_validator
from typing import Optional

from core_service.core_apis_server.schemas.base import BaseSchema


class TeamCreate(BaseSchema):
    name: str
    organization_id: int
    parent_id: Optional[int] = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if not v or v.isspace():
            raise ValueError("Team name cannot be empty")
        return v


class TeamUpdate(BaseSchema):
    name: Optional[str] = None
    organization_id: Optional[int] = None
    parent_id: Optional[int] = None


class TeamRead(BaseSchema):
    id: int
    name: str
    organization_id: int
    parent_id: Optional[int] = None
