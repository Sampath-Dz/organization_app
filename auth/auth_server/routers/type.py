
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.auth_server.services.type import TypeService
from auth.auth_server.dependencies import get_db


router = APIRouter(prefix="/auth/v1/types", tags=["Types"])


def get_type_service(db: Session = Depends(get_db)):
    return TypeService(db)


@router.post("")
def create_type(
    name: str,
    service: TypeService = Depends(get_type_service)
):
    type_obj = service.create_type(name)
    return {"id": type_obj.id, "name": type_obj.name}


@router.get("")
def list_types(
    service: TypeService = Depends(get_type_service)
):
    types = service.get_types()
    return [{"id": t.id, "name": t.name} for t in types]


@router.put("/{type_id}")
def update_type(
    type_id: int,
    name: str,
    service: TypeService = Depends(get_type_service)
):
    type_obj = service.update_type(type_id, name)
    return {"id": type_obj.id, "name": type_obj.name}


@router.delete("/{type_id}")
def delete_type(
    type_id: int,
    service: TypeService = Depends(get_type_service)
):
    service.delete_type(type_id)
    return {"detail": "Type deleted successfully"}
