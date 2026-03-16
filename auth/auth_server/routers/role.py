from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.role import RoleService
from ..models.models import Role
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/roles", tags=["Roles"])

@router.post("", response_model=dict)
def create_role(name: str, db: Session = Depends(get_db)):
    service = RoleService(db)
    try:
        role = service.create_role(name)
        return {"id": role.id, "name": role.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[dict])
def list_roles(db: Session = Depends(get_db)):
    service = RoleService(db)
    roles = service.get_roles()
    return [{"id": r.id, "name": r.name} for r in roles]

@router.put("/{role_id}", response_model=dict)
def update_role(role_id: int, name: str, db: Session = Depends(get_db)):
    service = RoleService(db)
    role = service.update_role(role_id, name)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"id": role.id, "name": role.name}

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    service = RoleService(db)
    success = service.delete_role(role_id)
    if not success:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"detail": "Role deleted successfully"}
