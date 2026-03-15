<<<<<<< HEAD
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .db_base import Base  # <-- make sure Base exists in db_base.py

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teams = relationship("Team", back_populates="organization")

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="teams")
    members = relationship("Member", back_populates="team")

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="members")
=======
from sqlalchemy import Column,String,Integer,ForeignKey

from .base_model import BaseModel


class Organization(BaseModel):

    __tablename__="organizations"

    name=Column(String,nullable=False)


class Team(BaseModel):

    __tablename__="teams"

    name=Column(String,nullable=False)

    organization_id=Column(Integer,ForeignKey("organizations.id"))


class Member(BaseModel):

    __tablename__="members"

    name=Column(String,nullable=False)

    team_id=Column(Integer,ForeignKey("teams.id"))
>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
