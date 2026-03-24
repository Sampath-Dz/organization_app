from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class BaseDB:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self._engine = None
        self._session_factory = None

    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(
                self.db_url,
                pool_pre_ping=True,
                pool_size=10,
                max_overflow=20
            )
        return self._engine

    def session(self):
        if self._session_factory is None:
            self._session_factory = scoped_session(
                sessionmaker(
                    bind=self.engine,
                    autocommit=False,
                    autoflush=False
                )
            )
        return self._session_factory