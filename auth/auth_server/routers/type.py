from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.type import TypeService
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/types", tags=["Types"])

@router.post("", response_model=dict)
def create_type(name: str, db: Session = Depends(get_db)):
    service = TypeService(db)
    try:
        type_obj = service.create_type(name)
        return {"id": type_obj.id, "name": type_obj.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[dict])
def list_types(db: Session = Depends(get_db)):
    service = TypeService(db)
    types = service.get_types()
    return [{"id": t.id, "name": t.name} for t in types]

@router.put("/{type_id}", response_model=dict)
def update_type(type_id: int, name: str, db: Session = Depends(get_db)):
    service = TypeService(db)
    type_obj = service.update_type(type_id, name)
    if not type_obj:
        raise HTTPException(status_code=404, detail="Type not found")
    return {"id": type_obj.id, "name": type_obj.name}

@router.delete("/{type_id}")
def delete_type(type_id: int, db: Session = Depends(get_db)):
    service = TypeService(db)
    success = service.delete_type(type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Type not found")
    return {"detail": "Type deleted successfully"}
