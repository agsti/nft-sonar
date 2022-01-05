from pydantic import BaseModel

from typing import Optional
from datetime import datetime


class Collection(BaseModel):
    id: Optional[int]
    slug: str
    name: Optional[str]
    telegram_url: Optional[str]
    twitter_username: Optional[str]
    created_at: datetime
    latest_fetch: datetime
