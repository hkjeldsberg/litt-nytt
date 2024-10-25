from typing import List

from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from sqlalchemy.orm import Session

from app.client.summary_client import SummaryService
from app.db import crud
from app.db.database import get_db
from app.models.summary_response import SummaryResponse
from app.service.extraction_service import ExtractionService

router = APIRouter()

extraction_service = ExtractionService()
summary_service = SummaryService()


@router.post("/update", response_model=List[SummaryResponse], name="update_summaries")
def update_summarize(db: Session = Depends(get_db)) -> List[SummaryResponse]:
    # Extract articles
    article_info = extraction_service.get_article_info()
    extraction_service.get_articles(article_info)

    # Filter articles already summarized
    existing_article_ids = crud.get_all_article_ids(db)
    new_articles = [article for article in article_info if article["article_id"] not in existing_article_ids]

    # Summarize articles
    summaries = summary_service.get_summaries(new_articles[:15])

    # Store new summaries
    created_summaries = [crud.create_summary(db=db, summary=summary) for summary in summaries[:1]]

    return created_summaries


@router.get("/summaries", response_model=List[SummaryResponse], name="get_all_summaries")
def get_all_summaries(db: Session = Depends(get_db)) -> List[SummaryResponse]:
    return crud.get_all_summaries(db)


@router.delete("/summaries/{article_id}", response_model=SummaryResponse, name="delete_summary")
def delete_summary(article_id: str, db: Session = Depends(get_db)) -> SummaryResponse:
    summary = crud.get_summary_by_article_id(db, article_id)
    if not summary:
        error_message = "Summary not found"
        logger.error(error_message)
        raise HTTPException(status_code=404, detail=error_message)

    return crud.delete_summary(db, article_id)
