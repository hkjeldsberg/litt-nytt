from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SummaryModel(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    url = Column(String, nullable=False)
    date = Column(String, nullable=False)
    article_id = Column(String, nullable=False)
