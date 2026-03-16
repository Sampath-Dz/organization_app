from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.base import BaseService
from ..schemas.role import RoleCreate, RoleRead
from ..models.models import Role
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/roles", tags=["Roles"])

@router.post("", response_model=RoleRead)
def create_role(data: RoleCreate, db: Session = Depends(get_db)):
    service = BaseService(db)
    role = Role(name=data.name)
    return service.create(role)
