from fastapi import APIRouter

from app.client.summary_client import SummaryService
from app.models.summary_response import SummaryResponse
from app.service.extraction_service import ExtractionService

router = APIRouter()

extraction_service = ExtractionService()
summary_service = SummaryService()


@router.get("", response_model=SummaryResponse, name="summarize")
def summarize() -> SummaryResponse:
    article_info = extraction_service.get_article_info()
    article_info = article_info[:5]

    extraction_service.get_articles(article_info)
    summaries = summary_service.get_summaries(article_info)

    return SummaryResponse(summaries=summaries)
