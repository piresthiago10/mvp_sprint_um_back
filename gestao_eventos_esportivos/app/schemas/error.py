from pydantic import BaseModel, Field


class ErrorSchema(BaseModel):
    """Define como uma mensagem de erro será representada."""

    message: str = Field(description="Menssagem de erro", example="Menssagem de erro")
