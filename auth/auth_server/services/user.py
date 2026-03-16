from .base import BaseService
from ..models.models import User
from ..utils import hash_password

class UserService(BaseService):
    def create_user(self, data):
        user = User(
            name=data.name,
            mail=data.mail,
            password=hash_password(data.password)
        )
        return self.create(user)

    def get_users(self):
        return self.db.query(User).all()

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()
