
from pydantic import BaseModel


class TokenRequest(BaseModel):
    user_id: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
