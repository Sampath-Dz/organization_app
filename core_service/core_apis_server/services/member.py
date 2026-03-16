from sqlalchemy.orm import Session
from ..models.models import Member
from ..crud.generic import create_item, get_all_items, get_item, update_item, delete_item

class MemberService:
    def __init__(self, db: Session):
        self.db = db

    def create_member(self, data: dict):
        return create_item(self.db, Member, data)

    def get_members(self):
        return get_all_items(self.db, Member)

    def get_member(self, member_id: int):
        return get_item(self.db, Member, member_id)

    def update_member(self, member_id: int, data: dict):
        member = self.get_member(member_id)
        if not member:
            return None
        for key, value in data.items():
            setattr(member, key, value)
        update_item(self.db)
        return member

    def delete_member(self, member_id: int):
        member = self.get_member(member_id)
        if not member:
            return False
        delete_item(self.db, member)
        return True
