from passlib.context import CryptContext
from .models.db_factory import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


from jose import jwt
from datetime import datetime,timedelta
from .settings import JWT_SECRET,JWT_ALGORITHM


def create_access_token(data:dict):

    to_encode=data.copy()

    expire=datetime.utcnow()+timedelta(minutes=60)

    to_encode.update({"exp":expire})

    token=jwt.encode(to_encode,JWT_SECRET,algorithm=JWT_ALGORITHM)

    return token
