from sqlalchemy import Column,String,Integer,ForeignKey
from .base_model import BaseModel


class User(BaseModel):

    __tablename__="users"

    name=Column(String)

    mail=Column(String,unique=True)

    password=Column(String)

    last_login=Column(String)



class Role(BaseModel):

    __tablename__="roles"

    name=Column(String)

    description=Column(String)



class Type(BaseModel):

    __tablename__="types"

    name=Column(String)

    description=Column(String)



class Assignment(BaseModel):

    __tablename__="assignments"

    user_id=Column(Integer,ForeignKey("users.id"))

    role_id=Column(Integer,ForeignKey("roles.id"))

    type_id=Column(Integer,ForeignKey("types.id"))

    resource_id=Column(Integer)
