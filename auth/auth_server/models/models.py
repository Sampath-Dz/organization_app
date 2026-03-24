import uuid
import time
from sqlalchemy import Column, String, Integer, Boolean, TEXT, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from auth.auth_server.models.db_base import Base

def generate_uuid():
    return str(uuid.uuid4())

def current_timestamp():
    return int(time.time())

def gen_salt() -> str:
    import string, random
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

class BaseModel:
    id = Column(String(36), primary_key=True, default=generate_uuid)
    created_at = Column(Integer, nullable=False, default=current_timestamp)
    deleted_at = Column(Integer, default=0, nullable=False)

    @hybrid_property
    def deleted(self) -> bool:
        return self.deleted_at != 0

class Type(Base, BaseModel):
    __tablename__ = 'type'
    parent_id  = Column(Integer, ForeignKey('type.id'), nullable=True)
    name       = Column(String(64), nullable=False, unique=True)
    assignable = Column(Boolean, nullable=False, default=True)
    children = relationship('Type', cascade='all', backref=backref('parent', remote_side='Type.id'), collection_class=list)

    @hybrid_property
    def child_tree(self) -> list:
        all_ = []
        def get_children(node, li):
            if node:
                items = node.children
                if len(items) == 1:
                    li.append(items[0])
                    get_children(items[0], li)
                elif len(items) > 1:
                    from auth.auth_server.exceptions import InvalidTreeException
                    raise InvalidTreeException("Invalid tree format")
        get_children(self, all_)
        return sorted(all_, key=lambda x: x.id)

    @hybrid_property
    def parent_tree(self) -> list:
        all_ = []
        def get_parents(node, li):
            if node:
                element = node.parent
                if element:
                    all_.append(element)
                    get_parents(element, li)
        get_parents(self, all_)
        return sorted(all_, key=lambda x: x.id, reverse=True)

    def __init__(self, id_=None, name=None, parent=None, assignable=True):
        self.id = id_
        self.name = name
        self.parent = parent
        self.assignable = assignable

class User(Base, BaseModel):
    __tablename__ = 'user'
    mail       = Column(String(256), nullable=False, index=True)
    name       = Column(String(256), nullable=False)
    password   = Column(String(64), nullable=False)
    salt       = Column(String(20), nullable=False)
    is_active  = Column(Boolean, nullable=False, default=True)
    last_login = Column(Integer, nullable=True, default=None)
    type_id    = Column(Integer, ForeignKey('type.id'), nullable=True)
    type = relationship('Type', backref='users')
    assignments = relationship('Assignment', back_populates='user', primaryjoin='and_(User.id == Assignment.user_id, Assignment.deleted_at == 0)', lazy='dynamic')

    __table_args__ = (UniqueConstraint('mail', 'deleted_at', name='idx_user_mail_deleted_at'),)

    def __init__(self, mail=None, name=None, password=None, salt=None, type_=None, type_id=None, is_active=True, last_login=None):
        if type_:
            self.type = type_
        if type_id is not None:
            self.type_id = type_id
        self.mail = mail
        self.name = name
        self.password = password
        self.salt = salt if salt else gen_salt()
        self.is_active = is_active
        self.last_login = last_login

class Role(Base, BaseModel):
    __tablename__ = 'role'
    name        = Column(String(64), nullable=False, index=True)
    description = Column(TEXT, nullable=True)
    type_id     = Column(Integer, ForeignKey('type.id'), nullable=True)
    is_active   = Column(Boolean, nullable=False, default=True)
    shared      = Column(Boolean, nullable=False, default=False)
    type = relationship('Type', backref='roles')
    assignments = relationship('Assignment', back_populates='role', primaryjoin='and_(Role.id == Assignment.role_id, Assignment.deleted_at == 0)', lazy='dynamic')

    __table_args__ = (UniqueConstraint('name', 'type_id', 'deleted_at', name='idx_role_name_type_deleted'),)

    def __init__(self, name=None, description=None, type_=None, type_id=None, is_active=True, shared=False):
        if type_:
            self.type = type_
        if type_id is not None:
            self.type_id = type_id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.shared = shared

class Assignment(Base, BaseModel):
    __tablename__ = 'assignment'
    type_id     = Column(Integer, ForeignKey('type.id'), nullable=False)
    role_id     = Column(Integer, ForeignKey('role.id'), nullable=False)
    user_id     = Column(String(36), ForeignKey('user.id'), nullable=False)
    resource_id = Column(String(36), nullable=True, index=True)
    user = relationship('User', back_populates='assignments')
    role = relationship('Role', back_populates='assignments')
    type = relationship('Type', backref='assignments')

    __table_args__ = (UniqueConstraint('user_id', 'resource_id', 'role_id', 'type_id', 'deleted_at', name='uq_assignment_user_role_resource_active'),)

    def __init__(self, user=None, role=None, type_=None, resource_id=None, role_id=None, type_id=None, user_id=None):
        if user:
            self.user = user
        if user_id is not None:
            self.user_id = user_id
        if role:
            self.role = role
        if role_id is not None:
            self.role_id = role_id
        if type_:
            self.type = type_
        if type_id is not None:
            self.type_id = type_id
        self.resource_id = resource_id