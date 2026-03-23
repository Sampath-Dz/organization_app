import logging
import uuid
from fastapi import Request
from sqlalchemy.orm import Session

from auth.auth_server.models.models import User
from auth.auth_server.services.base import BaseService
from auth.auth_server.utils import hash_password, verify_password, get_current_timestamp
from auth.auth_server.exceptions import Err, ConflictException, UnauthorizedException, NotFoundException
from auth.auth_server.schemas.user import UserCreate, UserUpdate

LOG = logging.getLogger(__name__)


class UserService(BaseService):

    def __init__(self, db: Session, request: Request = None, **kwargs):
        super().__init__(db)
        self._session = db
        self.request = request

    def _get_model_type(self):
        return User

    def get_by_mail(self, mail: str) -> User | None:
        return self._session.query(User).filter(
            User.mail == mail,
            User.deleted_at == None
        ).first()

    def get_by_id(self, user_id: str) -> User:
        user = self._session.query(User).filter(
            User.id == user_id,
            User.deleted_at == None
        ).first()

        if not user:
            raise NotFoundException(Err.AUTH0003, ["User", user_id])

        return user

    def create_user(self, data: UserCreate) -> User:
        if self.get_by_mail(data.email):
            raise ConflictException(Err.AUTH0007, ["User"])

        user = User(
            id=str(uuid.uuid4()),
            mail=data.email,
            name=data.name,
            password=hash_password(data.password),
            created_at=get_current_timestamp(),
            deleted_at=None
        )

        return self.save(user)

    def update_user(self, user_id: str, data: UserUpdate) -> User:
        user = self.get_by_id(user_id)

        if data.name is not None:
            user.name = data.name

        if data.email is not None:
            existing = self.get_by_mail(data.email)
            if existing and existing.id != user_id:
                raise ConflictException(Err.AUTH0007, ["Email"])
            user.mail = data.email

        if data.password is not None:
            user.password = hash_password(data.password)

        return self.update(user)

    def patch_user(self, user_id: str, data: UserUpdate):
        return self.update_user(user_id, data)

    def delete_user(self, user_id: str):
        user = self.get_by_id(user_id)
        user.deleted_at = get_current_timestamp()
        self._session.commit()

    def authenticate(self, mail: str, password: str) -> User:
        user = self.get_by_mail(mail)

        if not user:
            raise UnauthorizedException(Err.AUTH0006)

        if not verify_password(password, user.password):
            raise UnauthorizedException(Err.AUTH0006)

        user.last_login = get_current_timestamp()
        self._session.commit()

        return user