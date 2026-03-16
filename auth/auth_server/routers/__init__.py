from fastapi import APIRouter
from .user import router as user_router
from .assignment import router as assignment_router
from .token import router as token_router
from .role import router as role_router
from .type import router as type_router

router = APIRouter()
router.include_router(user_router)
router.include_router(assignment_router)
router.include_router(token_router)
router.include_router(role_router)
router.include_router(type_router)
