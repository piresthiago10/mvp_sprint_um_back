from pydantic import BaseModel, Field
from datetime import date
from typing import List

from app.schemas.endereco import EnderecoBase
from app.schemas.trajeto import TrajetoBase


class EventoBase(BaseModel):
    """Define como um evento será representado."""

    nome: str = Field(
        description="Nome do evento", example="Caminhada pela saúde", max_length=140
    )
    data: date = Field(description="Data do evento", example="2022-02-02")
    trajeto: TrajetoBase = Field(description="Trajeto do evento")
    endereco: EnderecoBase = Field(description="Endereco do evento")

    class Config:
        orm_mode = True
