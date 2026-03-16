from pydantic import BaseModel

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
