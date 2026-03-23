
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.auth_server.services.token import TokenService
from auth.auth_server.models.db_factory import get_db


router = APIRouter(prefix="/auth/v1/token", tags=["Token"])


def get_token_service(db: Session = Depends(get_db)):
    return TokenService(db)


@router.post("")
def generate_token(
    user_id: int,
    service: TokenService = Depends(get_token_service)
):
    access_token = service.create_access_token({"user_id": user_id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/decode")
def decode_token(
    token: str,
    service: TokenService = Depends(get_token_service)
):
    return service.decode_access_token(token)
