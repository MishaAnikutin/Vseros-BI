from fastapi import APIRouter

from .handlers.informatics import informatics_router

router = APIRouter(prefix="/v1")
router.include_router(informatics_router, prefix="/informatics")

__all__ = ["router"]
