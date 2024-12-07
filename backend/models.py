from datetime import datetime

from pydantic import BaseModel, Field


class Item(BaseModel):
    item_name: str
    item_id: int
    brand_name: str
    rest_count: int
    timestamp: datetime = Field(default_factory=datetime.now)


class ItemCollection(BaseModel):
    items: list[Item]
