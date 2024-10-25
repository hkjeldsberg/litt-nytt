from loguru import logger
from sqlalchemy.orm import Session

from app.models.summary_create import SummaryCreate
from app.models.summary_model import SummaryModel


def create_summary(db: Session, summary: SummaryCreate):
    logger.debug("Storing summary")
    db_summary = SummaryModel(**summary)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return db_summary


def get_all_article_ids(db: Session):
    logger.debug("Fetching all article ids")
    return [result[0] for result in db.query(SummaryModel.article_id).all()]


def get_all_summaries(db: Session):
    logger.debug("Fetching all summaries")
    return db.query(SummaryModel).all()


def get_summary_by_article_id(db: Session, article_id: str):
    logger.debug("Fetching summaries by article id")
    return db.query(SummaryModel).filter(SummaryModel.article_id == article_id).first()


def delete_summary(db: Session, article_id: str):
    summary = get_summary_by_article_id(db, article_id)
    if summary:
        db.delete(summary)
        db.commit()
    return summary
