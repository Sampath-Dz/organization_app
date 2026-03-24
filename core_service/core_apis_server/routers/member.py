from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from core_service.core_apis_server.schemas.member import (
    MemberCreate,
    MemberUpdate,
    MemberResponse,
    MemberListResponse
)
from core_service.core_apis_server.services.member import MemberService
from core_service.core_apis_server.models.db_factory import DBFactory

router = APIRouter(prefix="/core/v1/members", tags=["Members"])

def get_service(db: Session = Depends(DBFactory().get_db)):
    return MemberService(db)

@router.post("", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(data: MemberCreate, service: MemberService = Depends(get_service)):
    return service.create_member(data)

@router.get("", response_model=List[MemberResponse])
def list_members(service: MemberService = Depends(get_service)):
    return service.get_members()

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: str, service: MemberService = Depends(get_service)):
    return service.get_member(member_id)

@router.put("/{member_id}", response_model=MemberResponse)
def update_member(member_id: str, data: MemberUpdate, service: MemberService = Depends(get_service)):
    return service.update_member(member_id, data)

@router.patch("/{member_id}", response_model=MemberResponse)
def patch_member(member_id: str, data: MemberUpdate, service: MemberService = Depends(get_service)):
    return service.patch_member(member_id, data)

@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: str, service: MemberService = Depends(get_service)):
    service.delete_member(member_id)
    return {"detail": "Member deleted"}