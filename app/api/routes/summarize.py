from fastapi import APIRouter

from app.extraction_service import ExtractionService
from app.models.health import HealthResponse
from app.summary_response import SummaryResponse
from app.summary_service import SummaryService

router = APIRouter()

extraction_service = ExtractionService()
summary_service = SummaryService()


@router.get("", response_model=HealthResponse, name="health")
def summarize() -> SummaryResponse:
    urls = extraction_service.get_urls()
    urls = urls[:2]
    articles = extraction_service.get_articles(urls)
    summaries = summary_service.get_summaries(articles)

    return SummaryResponse(summaries=summaries)
