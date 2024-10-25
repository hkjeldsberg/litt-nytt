from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy.orm import Session

from app.client.summary_client import SummaryService
from app.db import crud
from app.db.database import get_db
from app.models.summary_create import SummaryCreate
from app.models.summary_response import SummaryResponse
from app.service.extraction_service import ExtractionService

router = APIRouter()

extraction_service = ExtractionService()
summary_service = SummaryService()


@router.post("", response_model=SummaryResponse, name="summarize")
def summarize(db: Session = Depends(get_db)) -> SummaryResponse:
    article_info = extraction_service.get_article_info()
    article_info = article_info[:1]

    extraction_service.get_articles(article_info)
    summaries = summary_service.get_summaries(article_info)
    summary = summaries[0]

    response = crud.create_summary(db=db, summary=summary)
    logger.warning(response)
    return response


@router.post("", response_model=SummaryResponse, name="summarize")
def create_summary(summary: SummaryCreate, db: Session = Depends(get_db)) -> SummaryResponse:
    return crud.create_summary(db, summary)


def update_summary():
    pass


def delete_summary():
    pass


def get_summaries():
    pass


def get_summary():
    pass
