from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from core_service.core_apis_server.schemas.org import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
    OrganizationListResponse
)
from core_service.core_apis_server.services.org import OrganizationService
from core_service.core_apis_server.models.db_factory import DBFactory

router = APIRouter(prefix="/core/v1/organizations", tags=["Organizations"])

def get_service(db: Session = Depends(DBFactory().get_db)):
    return OrganizationService(db)

@router.post("", response_model=OrganizationResponse, status_code=status.HTTP_201_CREATED)
def create_organization(data: OrganizationCreate, service: OrganizationService = Depends(get_service)):
    return service.create_organization(data)

@router.get("", response_model=List[OrganizationResponse])
def list_organizations(service: OrganizationService = Depends(get_service)):
    return service.get_organizations()

@router.get("/{org_id}", response_model=OrganizationResponse)
def get_organization(org_id: str, service: OrganizationService = Depends(get_service)):
    return service.get_organization(org_id)

@router.put("/{org_id}", response_model=OrganizationResponse)
def update_organization(org_id: str, data: OrganizationUpdate, service: OrganizationService = Depends(get_service)):
    return service.update_organization(org_id, data)

@router.patch("/{org_id}", response_model=OrganizationResponse)
def patch_organization(org_id: str, data: OrganizationUpdate, service: OrganizationService = Depends(get_service)):
    return service.patch_organization(org_id, data)

@router.delete("/{org_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_organization(org_id: str, service: OrganizationService = Depends(get_service)):
    service.delete_organization(org_id)
    return {"detail": "Organization deleted"}