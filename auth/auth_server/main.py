from fastapi import FastAPI

from .routers import router
from .models.db_base import Base, engine


app = FastAPI(title="Auth Service")


Base.metadata.create_all(bind=engine)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "auth.auth_server.main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
