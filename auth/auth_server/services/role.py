
from auth.auth_server.services.base import BaseService
from auth.auth_server.models.models import Role


class RoleService(BaseService):

    def get_role_by_id(self, role_id: int):
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise Exception("Role not found")
        return role

    def create_role(self, name: str):
        existing = self.db.query(Role).filter(Role.name == name).first()
        if existing:
            raise Exception("Role already exists")

        role = Role(name=name)
        return self.create(role)

    def get_roles(self):
        return self.db.query(Role).all()

    def update_role(self, role_id: int, name: str):
        role = self.get_role_by_id(role_id)
        role.name = name
        return self.update(role)

    def delete_role(self, role_id: int):
        role = self.get_role_by_id(role_id)
        self.delete(role)
        return True
