from pydantic import BaseModel

class MemberCreate(BaseModel):
    name: str
    team_id: int

class MemberRead(BaseModel):
    id: int
    name: str
    team_id: int

    model_config = {"from_attributes": True}
