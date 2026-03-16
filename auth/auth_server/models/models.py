from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db_base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    resource_id = Column(Integer, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    role = relationship("Role")
    type = relationship("Type")
    user = relationship("User")
