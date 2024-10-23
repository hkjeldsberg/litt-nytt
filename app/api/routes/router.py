from fastapi import APIRouter

from app.api.routes import health, summarize

router = APIRouter()
router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(summarize.router, prefix="/summarize", tags=["summary"])
