from .base import BaseService
from ..models.models import Type

class TypeService(BaseService):

    def create_type(self, name: str):
        existing = self.db.query(Type).filter(Type.name == name).first()
        if existing:
            raise Exception("Type already exists")
        type_obj = Type(name=name)
        return self.create(type_obj)

    def get_types(self):
        return self.db.query(Type).all()

    def get_type(self, type_id: int):
        return self.db.query(Type).filter(Type.id == type_id).first()

    def update_type(self, type_id: int, name: str):
        type_obj = self.get_type(type_id)
        if not type_obj:
            return None
        type_obj.name = name
        self.update()
        return type_obj

    def delete_type(self, type_id: int):
        type_obj = self.get_type(type_id)
        if not type_obj:
            return False
        self.delete(type_obj)
        return True
