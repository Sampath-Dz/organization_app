from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_apis_server.models.models import Member
from core_apis_server.models.db_factory import get_db
from core_apis_server.crud.generic import create_item, get_all_items, get_item, update_item, delete_item

router = APIRouter(prefix="/core/v1/members", tags=["Members"])

@router.post("")
def create_member(data: dict, db: Session = Depends(get_db)):
    return create_item(db, Member, data)

@router.get("")
def list_members(db: Session = Depends(get_db)):
    return get_all_items(db, Member)

@router.get("/{member_id}")
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = get_item(db, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.put("/{member_id}")
def update_member(member_id: int, data: dict, db: Session = Depends(get_db)):
    member = get_item(db, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return update_item(db, member, data)

@router.patch("/{member_id}")
def patch_member(member_id: int, data: dict, db: Session = Depends(get_db)):
    member = get_item(db, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return update_item(db, member, data)

@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = get_item(db, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    delete_item(db, member)
    return {"detail": "Deleted successfully"}
