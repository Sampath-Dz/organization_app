from .base import BaseService
from ..models.models import Role

class RoleService(BaseService):

    def create_role(self, name: str):
        existing = self.db.query(Role).filter(Role.name == name).first()
        if existing:
            raise Exception("Role already exists")
        role = Role(name=name)
        return self.create(role)

    def get_roles(self):
        return self.db.query(Role).all()

    def get_role(self, role_id: int):
        return self.db.query(Role).filter(Role.id == role_id).first()

    def update_role(self, role_id: int, name: str):
        role = self.get_role(role_id)
        if not role:
            return None
        role.name = name
        self.update()
        return role

    def delete_role(self, role_id: int):
        role = self.get_role(role_id)
        if not role:
            return False
        self.delete(role)
        return True
