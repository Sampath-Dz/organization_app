
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.auth_server.services.role import RoleService
from auth.auth_server.models.db_factory import get_db


router = APIRouter(prefix="/auth/v1/roles", tags=["Roles"])


def get_role_service(db: Session = Depends(get_db)):
    return RoleService(db)


@router.post("")
def create_role(
    name: str,
    service: RoleService = Depends(get_role_service)
):
    role = service.create_role(name)
    return {"id": role.id, "name": role.name}


@router.get("")
def list_roles(
    service: RoleService = Depends(get_role_service)
):
    roles = service.get_roles()
    return [{"id": r.id, "name": r.name} for r in roles]


@router.put("/{role_id}")
def update_role(
    role_id: int,
    name: str,
    service: RoleService = Depends(get_role_service)
):
    role = service.update_role(role_id, name)
    return {"id": role.id, "name": role.name}


@router.delete("/{role_id}")
def delete_role(
    role_id: int,
    service: RoleService = Depends(get_role_service)
):
    service.delete_role(role_id)
    return {"detail": "Role deleted successfully"}
