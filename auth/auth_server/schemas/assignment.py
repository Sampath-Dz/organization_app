
from pydantic import BaseModel, ConfigDict


class AssignmentCreate(BaseModel):
    resource_id: int
    role_id: int
    type_id: int
    user_id: int


class AssignmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    resource_id: int
    role_id: int
    type_id: int
    user_id: int


class AssignmentListResponse(BaseModel):
    assignments: list[AssignmentResponse]
    total: int
