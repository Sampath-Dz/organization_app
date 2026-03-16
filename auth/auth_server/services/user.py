from .base import BaseService
from ..models.models import User
from ..schemas.user import UserCreate

class UserService(BaseService):

    def create_user(self, data: UserCreate):
        existing = self.db.query(User).filter(User.mail == data.mail).first()
        if existing:
            raise Exception("User already exists")
        user = User(name=data.name, mail=data.mail, password=data.password)
        return self.create(user)

    def get_users(self):
        return self.db.query(User).all()

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: int, data: UserCreate):
        user = self.get_user(user_id)
        if not user:
            return None
        user.name = data.name
        user.mail = data.mail
        user.password = data.password
        self.update()
        return user

    def patch_user(self, user_id: int, data: dict):
        user = self.get_user(user_id)
        if not user:
            return None
        if "name" in data:
            user.name = data["name"]
        if "mail" in data:
            user.mail = data["mail"]
        if "password" in data:
            user.password = data["password"]
        self.update()
        return user

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        if not user:
            return False
        self.delete(user)
        return True
