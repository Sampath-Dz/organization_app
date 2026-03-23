import sys
import os
import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core_service.core_apis_server.settings import settings
from core_service.core_apis_server.middleware import LoggingMiddleware
from core_service.core_apis_server.routers import router
from core_service.core_apis_server.models.db_postgre import postgres_db

LOG = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    LOG.info("Starting Core Service...")
    yield
    LOG.info("Shutting down Core Service.")

app = FastAPI(
    title=settings.CORE_APP_TITLE,
    version=settings.CORE_APP_VERSION,
    debug=settings.CORE_DEBUG,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "db": postgres_db.ping()}

if __name__ == "__main__":
    uvicorn.run(
        "core_service.core_apis_server.main:app",
        host=settings.CORE_APP_HOST,
        port=settings.CORE_APP_PORT,
        reload=True
    )