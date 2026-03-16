from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..schemas.user import UserCreate, UserRead, UserUpdate
from ..services.user import UserService
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/users", tags=["Users"])

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(data)


@router.get("", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_users()


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    updated_user = service.update_user(user_id, data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.patch("/{user_id}", response_model=UserRead)
def patch_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    patched_user = service.patch_user(user_id, data)
    if not patched_user:
        raise HTTPException(status_code=404, detail="User not found")
    return patched_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
