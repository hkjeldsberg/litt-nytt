from fastapi import APIRouter

from app.models.health_response import HealthResponse

router = APIRouter()


@router.get("", response_model=HealthResponse, name="health")
def health_check() -> HealthResponse:
    health = HealthResponse(is_healthy=True)

    return health
