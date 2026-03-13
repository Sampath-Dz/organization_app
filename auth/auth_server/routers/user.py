from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..utils import get_db
from ..schemas.user import UserCreate
from ..services.user import UserService

router=APIRouter(prefix="/auth/v1/users")

service=UserService()


@router.post("")
def create_user(data:UserCreate,db:Session=Depends(get_db)):

    return service.create_user(db,data)



from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from ..utils import get_db
from ..schemas.user import UserCreate
from ..models.models import User
from ..services.user import UserService

router=APIRouter(prefix="/auth/v1/users")

service=UserService()


# create user
@router.post("")
def create_user(data:UserCreate,db:Session=Depends(get_db)):

    return service.create_user(db,data)


# get all users
@router.get("")
def get_users(db:Session=Depends(get_db)):

    return db.query(User).all()


# get user by id
@router.get("/{id}")
def get_user(id:int,db:Session=Depends(get_db)):

    return db.query(User).filter(User.id==id).first()


# update user
@router.patch("/{id}")
def update_user(id:int,data:UserCreate,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.id==id).first()

    user.name=data.name
    user.mail=data.mail

    db.commit()

    return user


# delete user
@router.delete("/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.id==id).first()

    db.delete(user)

    db.commit()

    return {"message":"deleted"}

