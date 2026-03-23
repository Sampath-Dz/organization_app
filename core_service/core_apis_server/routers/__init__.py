from fastapi import APIRouter

from core_service.core_apis_server.routers import org
from core_service.core_apis_server.routers import team
from core_service.core_apis_server.routers import member

router = APIRouter()

router.include_router(org.router)
router.include_router(team.router)
router.include_router(member.router)
