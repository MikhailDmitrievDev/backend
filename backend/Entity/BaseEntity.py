from pydantic import BaseModel


class BaseEntity(BaseModel):
    """Base entity inherit for BaseModel pydantic."""
    id: int
