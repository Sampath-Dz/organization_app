from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    mail: str
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    mail: str

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    name: Optional[str]
    mail: Optional[str]
    password: Optional[str]
