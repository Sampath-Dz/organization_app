
from auth.auth_server.services.base import BaseService
from auth.auth_server.models.models import Type


class TypeService(BaseService):

    def get_type_by_id(self, type_id: int):
        type_obj = self.db.query(Type).filter(Type.id == type_id).first()
        if not type_obj:
            raise Exception("Type not found")
        return type_obj

    def create_type(self, name: str):
        existing = self.db.query(Type).filter(Type.name == name).first()
        if existing:
            raise Exception("Type already exists")

        type_obj = Type(name=name)
        return self.create(type_obj)

    def get_types(self):
        return self.db.query(Type).all()

    def update_type(self, type_id: int, name: str):
        type_obj = self.get_type_by_id(type_id)
        type_obj.name = name
        return self.update(type_obj)

    def delete_type(self, type_id: int):
        type_obj = self.get_type_by_id(type_id)
        self.delete(type_obj)
        return True
