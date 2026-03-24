from passlib.context import CryptContext
from datetime import datetime, timezone
import jwt

from auth.auth_server.models.enums import TokenType
from auth.auth_server.exceptions import InvalidTokenException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def get_current_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def decode_token(token: str, token_type: TokenType) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != token_type.value:
            raise InvalidTokenException("Token type mismatch")
        return payload.get("sub")  # usually user_id
    except jwt.ExpiredSignatureError:
        raise InvalidTokenException("Token expired")
    except jwt.InvalidTokenError:
        raise InvalidTokenException("Invalid token")