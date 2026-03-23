import os
import logging
from alembic.config import Config
from alembic import command

LOG = logging.getLogger(__name__)


class Migrator:

    def __init__(self, engine):
        self.engine_url = str(engine.url)

        self.alembic_cfg = Config()
        self.alembic_cfg.set_main_option(
            "script_location",
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                "..",
                "alembic"
            ),
        )
        self.alembic_cfg.set_main_option(
            "sqlalchemy.url",
            self.engine_url
        )

    def migrate(self):
        LOG.info("Running Core migrations...")
        command.upgrade(self.alembic_cfg, "head")
        LOG.info("Core migrations completed.")

    def migrate_all(self):
        try:
            self.migrate()
        except Exception as e:
            LOG.error("Core migration failed: %s", e)
            raise
