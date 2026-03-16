from pydantic import BaseModel

class TokenRequest(BaseModel):
    user_id: int

class TokenResponse(BaseModel):
    token: str
