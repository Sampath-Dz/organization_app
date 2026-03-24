from pydantic import BaseModel, ConfigDict

class MemberCreate(BaseModel):
    auth_user_id: str
    team_id: str

class MemberUpdate(BaseModel):
    auth_user_id: Optional[str] = None
    team_id: Optional[str] = None

class MemberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    auth_user_id: str
    team_id: str
    created_at: int
    deleted_at: int

class MemberListResponse(BaseModel):
    members: list[MemberResponse]
    total: int