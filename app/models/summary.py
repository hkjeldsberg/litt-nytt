from pydantic import BaseModel


class Summary(BaseModel):
    id: str
    title: str
    summary: str
    url: str
    date: str
    article_id: str
