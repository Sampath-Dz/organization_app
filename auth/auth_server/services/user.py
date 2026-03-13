from .base import BaseService
from ..models.models import User
from ..exceptions import UserAlreadyExists
from ..utils import hash_password



class UserService(BaseService):

    def create_user(self,db,data):

        existing=db.query(User).filter(User.mail==data.mail).first()

        if existing:

            raise UserAlreadyExists()

        user=User(

            name=data.name,

            mail=data.mail,

            password=hash_password(data.password)

        )

        return self.create(db,user)
