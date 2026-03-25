import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from auth.auth_server.settings import settings
from auth.auth_server.middleware import LoggingMiddleware
from auth.auth_server.routers import routers
from auth.auth_server.models.db_postgre import postgres_db

LOG = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    LOG.info("Starting Auth Service...")
    LOG.info("Database schema ready.")
    yield
    LOG.info("Shutting down Auth Service.")

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
app.include_router(routers)

@app.get("/health")
def health():
    return {"status": "ok", "db": postgres_db.ping()}

if __name__ == "__main__":
    uvicorn.run(
        "auth.auth_server.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )
