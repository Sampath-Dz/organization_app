from fastapi import FastAPI
from auth_server.routers import router  
import uvicorn

def create_app() -> FastAPI:
    app = FastAPI(title="Auth Service")

   
    app.include_router(router)

    return app

app = create_app()

if __name__ == "__main__":
    
    uvicorn.run("auth_server.main:app", host="127.0.0.1", port=8001, reload=True)
