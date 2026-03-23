from sqlalchemy import create_engine
from core_service.core_apis_server.models.db_base import BaseDB
from core_service.core_apis_server.settings import settings

class PostgresDB(BaseDB):

    @property
    def engine(self):
        if not self._engine:
            self._engine = create_engine(
                settings.DATABASE_URL,
                pool_size=20,
                max_overflow=10,
                pool_recycle=300,
                pool_pre_ping=True
            )
        return self._engine


postgres_db = PostgresDB(settings.DATABASE_URL)