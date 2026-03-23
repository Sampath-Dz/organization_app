from fastapi import APIRouter
from auth.auth_server.routers import user, assignment, token, role, type

routers = APIRouter()
routers.include_router(user.router)
routers.include_router(assignment.router)
routers.include_router(token.router)
routers.include_router(role.router)
routers.include_router(type.router)
