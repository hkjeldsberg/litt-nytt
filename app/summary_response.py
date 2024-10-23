from typing import List

from pydantic import BaseModel


class SummaryResponse(BaseModel):
    summaries: List[dict]
