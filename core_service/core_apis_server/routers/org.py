from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.org import OrganizationCreate, OrganizationRead
from ..services.org import OrganizationService
from ..models.db_factory import get_db

router = APIRouter(prefix="/core/v1/organizations", tags=["Organizations"])

@router.post("", response_model=OrganizationRead)
def create_organization(data: OrganizationCreate, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.create_organization(data.dict())

@router.get("", response_model=list[OrganizationRead])
def get_organizations(db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.get_organizations()

@router.get("/{org_id}", response_model=OrganizationRead)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.get_organization(org_id)

@router.put("/{org_id}", response_model=OrganizationRead)
def update_organization(org_id: int, data: OrganizationCreate, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.update_organization(org_id, data.dict())

@router.patch("/{org_id}", response_model=OrganizationRead)
def patch_organization(org_id: int, data: dict, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.update_organization(org_id, data)

@router.delete("/{org_id}")
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return {"success": service.delete_organization(org_id)}
