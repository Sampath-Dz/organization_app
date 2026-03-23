
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from auth.auth_server.schemas.user import UserCreate, UserRead, UserUpdate
from auth.auth_server.services.user import UserService
from auth.auth_server.models.db_factory import get_db


router = APIRouter(prefix="/auth/v1/users", tags=["Users"])


def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create_user(data)


@router.get("", response_model=List[UserRead])
def list_users(
    service: UserService = Depends(get_user_service)
):
    return service.get_users()


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    return service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    return service.update_user(user_id, data)


@router.patch("/{user_id}", response_model=UserRead)
def patch_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    return service.patch_user(user_id, data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    service.delete_user(user_id)
    return {"detail": "User deleted successfully"}
