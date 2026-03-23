from sqlalchemy import inspect
from datetime import datetime, timezone

def as_dict(obj) -> dict:
    return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}

def get_current_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())
