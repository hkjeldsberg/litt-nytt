from sqlalchemy.orm import Session

from app.models.summary_create import SummaryCreate
from app.models.summary_model import SummaryModel


def create_summary(db: Session, summary: SummaryCreate):
    db_summary = SummaryModel(**summary)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return db_summary
