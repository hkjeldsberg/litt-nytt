from pydantic import BaseModel


class SummaryBase(BaseModel):
    title: str
    summary: str
    url: str
    date: str
    article_id: str
