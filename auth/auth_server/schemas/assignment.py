from pydantic import BaseModel

class AssignmentCreate(BaseModel):
    resource_id: int
    role_id: int
    type_id: int
    user_id: int

class AssignmentRead(BaseModel):
    id: int
    resource_id: int
    role_id: int
    type_id: int
    user_id: int

    model_config = {"from_attributes": True}
