from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.base import BaseService
from ..schemas.type import TypeCreate, TypeRead
from ..models.models import Type
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/types", tags=["Types"])

@router.post("", response_model=TypeRead)
def create_type(data: TypeCreate, db: Session = Depends(get_db)):
    service = BaseService(db)
    type_obj = Type(name=data.name)
    return service.create(type_obj)
