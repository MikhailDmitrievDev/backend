from datetime import datetime

from backend.Entity.BaseEntity import BaseEntity


class NewsEntity(BaseEntity):
    """Entity News."""
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
