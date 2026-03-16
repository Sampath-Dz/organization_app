from fastapi import FastAPI
from .routers import router

app = FastAPI(title="Auth Service")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("auth_service.main:app", host="127.0.0.1", port=8001, reload=True)
