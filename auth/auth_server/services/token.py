from jose import jwt
from datetime import datetime, timedelta
from ..globals import SECRET, ALGORITHM
from ..settings import ACCESS_TOKEN_EXPIRE_MINUTES

def create_token(user_id: int):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)
