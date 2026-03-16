from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserRead  # ✅ correct
from ..services.user import UserService
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/users", tags=["Users"])

@router.post("", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(data)

@router.get("", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_users()


