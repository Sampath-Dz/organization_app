from fastapi import APIRouter
from ..services.token import create_token

router = APIRouter(prefix="/auth/v1/token", tags=["Token"])

@router.post("")
def generate(user_id: int):
    return {"access_token": create_token(user_id)}
