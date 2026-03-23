import logging
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy import text
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

LOG = logging.getLogger(__name__)

Base = declarative_base()


class BaseDB:

    def __init__(self, config=None, scopefunc=None):
        self._engine = None
        self._config = config
        self._scopefunc = scopefunc
        self._session = None

    @property
    def engine(self) -> Engine:
        if not self._engine:
            self._engine = self._get_engine()
        return self._engine

    def get_session(self):
        if not self._session:
            self._session = scoped_session(
                sessionmaker(bind=self.engine),
                scopefunc=self._scopefunc
            )
        return self._session

    @retry(
        stop=stop_after_attempt(20),
        wait=wait_fixed(1),
        retry=retry_if_exception_type(Exception)
    )
    def create_all(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)

    def ping(self) -> bool:
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception as e:
            LOG.error("Database ping failed: %s", e)
            return False

    def _get_engine(self):
        raise NotImplementedError