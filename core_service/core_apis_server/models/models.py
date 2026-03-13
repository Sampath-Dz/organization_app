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
