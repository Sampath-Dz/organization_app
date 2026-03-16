from fastapi import FastAPI
from core_apis_server.routers import router  
import uvicorn

def create_app() -> FastAPI:
    app = FastAPI(title="Core API Service")

    
    app.include_router(router)

    return app

app = create_app()

if __name__ == "__main__":
   
    uvicorn.run("core_apis_server.main:app", host="127.0.0.1", port=8002, reload=True)
