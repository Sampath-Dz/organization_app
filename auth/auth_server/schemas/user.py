from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):

    name:str

    mail:EmailStr

    password:str
