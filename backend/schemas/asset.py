from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Asset(BaseModel):
    id: Optional[int]
    url: str
    marketplace_url: str
    name: str
    contract_name: str
    erc: str
    filename: str
    hashed_at: datetime
    collection_id: int
    kind: str
