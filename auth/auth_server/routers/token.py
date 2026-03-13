from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from ..utils import get_db,verify_password,create_access_token
from ..models.models import User

router=APIRouter(prefix="/auth/v1/token")


@router.post("")
def login(mail:str,password:str,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.mail==mail).first()

    if not user:

        return {"error":"invalid email"}

    if not verify_password(password,user.password):

        return {"error":"invalid password"}

    token=create_access_token({"user_id":user.id})

    return {"access_token":token}
