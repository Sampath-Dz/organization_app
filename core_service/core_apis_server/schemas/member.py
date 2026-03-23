from pydantic import field_validator
from typing import Optional

from core_service.core_apis_server.schemas.base import BaseSchema


class MemberCreate(BaseSchema):
    auth_user_id: int
    team_id: int


class MemberUpdate(BaseSchema):
    auth_user_id: Optional[int] = None
    team_id: Optional[int] = None


class MemberRead(BaseSchema):
    id: int
    auth_user_id: int
    team_id: int
