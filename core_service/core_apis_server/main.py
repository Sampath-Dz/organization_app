from fastapi import FastAPI
from core_apis_server.routers import router
from core_apis_server.middleware import LoggingMiddleware

app = FastAPI(title="Core API Service")

app.add_middleware(LoggingMiddleware)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("core_apis_server.main:app", host="127.0.0.1", port=8002, reload=True)
