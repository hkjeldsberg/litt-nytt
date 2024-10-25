from typing import List

from pydantic import BaseModel

from app.models.summary import Summary


class SummariesResponse(BaseModel):
    summaries: List[Summary]
