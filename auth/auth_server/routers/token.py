from fastapi import APIRouter
from ..services.token import TokenService

router = APIRouter(prefix="/auth/v1/token", tags=["Token"])

@router.post("/generate")
def generate_token(user_id: int):
    access_token = TokenService.create_access_token({"user_id": user_id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/decode")
def decode_token(token: str):
    try:
        payload = TokenService.decode_access_token(token)
        return payload
    except Exception as e:
        return {"error": str(e)}
