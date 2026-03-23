from pydantic import field_validator
from typing import Optional

from core_service.core_apis_server.schemas.base import BaseSchema


class OrganizationCreate(BaseSchema):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if not v or v.isspace():
            raise ValueError("Organization name cannot be empty")
        return v


class OrganizationUpdate(BaseSchema):
    name: Optional[str] = None


class OrganizationRead(BaseSchema):
    id: int
    name: str
