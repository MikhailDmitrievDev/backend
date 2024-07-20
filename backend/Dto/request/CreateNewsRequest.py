from pydantic import BaseModel, field_validator

from backend.Exceptions.SybolsException import ErrorSymbolsException


class CreateNewsRequest(BaseModel):
    title: str
    description: str

    @field_validator("title")
    def validate_title(cls, title: str) -> str:
        """Title symbols validate."""
        if len(title) > 255:
            raise ErrorSymbolsException(f"The length of the title cannot exceed 255 characters")
        return title

    @field_validator("description")
    def validate_description(cls, desc: str) -> str:
        """Description symbols validate."""
        if len(desc) > 2048:
            raise ErrorSymbolsException(f"The length of the title cannot exceed 2048 characters")
        return desc
