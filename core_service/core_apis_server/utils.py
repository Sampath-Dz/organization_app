from sqlalchemy import inspect
from datetime import datetime, timezone
import jwt

def as_dict(obj) -> dict:
    return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}

def get_current_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def decode_token(token: str, secret_key: str, algorithm: str = "HS256") -> str:
    from core_service.core_apis_server.exceptions import InvalidTokenException
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload.get("sub")
    except Exception as e:
        raise InvalidTokenException(str(e))