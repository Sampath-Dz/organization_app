from sqlalchemy import create_engine
from auth.auth_server.models.db_base import BaseDB
from auth.auth_server.settings import settings
from auth.auth_server.models.migrator import Migrator


class PostgresDB(BaseDB):

    def _get_engine(self):
        return create_engine(
            settings.get_database_url(),
            pool_pre_ping=True
        )

    def create_schema(self):
        migrator = Migrator(self.engine)
        migrator.migrate_all()


postgres_db = PostgresDB()