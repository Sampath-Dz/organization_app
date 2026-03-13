from fastapi import APIRouter

from .user import router as user_router
from .token import router as token_router
from .assignment import router as assignment_router


router = APIRouter()

router.include_router(user_router)
router.include_router(token_router)
router.include_router(assignment_router)
