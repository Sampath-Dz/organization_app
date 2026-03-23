from passlib.context import CryptContext
from datetime import datetime, timezone
from sqlalchemy import inspect

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def get_current_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())


def as_dict(obj) -> dict:
    return {
        column.key: getattr(obj, column.key)
        for column in inspect(obj).mapper.column_attrs
    }
