from pydantic import BaseModel, Field, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


class EventoCriacaoResponse(BaseModel):
    """Define como será retornado a resposta da criação do evento."""

    id: int = Field(description="Id do evento", example=1)


class EventoListagem(BaseModel):
    """Define como será retornado a resposta da criação do evento."""

    id: int = Field(description="Id do evento", example=1)
    nome: str = Field(
        description="Nome do evento", example="Caminhada pela saúde", max_length=140
    )
    data: str = Field(description="Data do evento", example="02/02/2025")
    trajeto_id: int = Field(description="Id do trajeto", example=1)
    endereco_id: int = Field(description="Id do endereco", example=1)

    model_config = ConfigDict(from_attributes=True)


class EventoListagemResponse(BaseModel):
    """Define como será retornado a resposta da criação do evento."""

    eventos: List[EventoListagem]


class EventoPath(BaseModel):
    """Define como será um id recebido via path."""

    id: int = Field(..., description="Id do evento", example=1)


class SuccessMessage(BaseModel):
    """Define como será retornado a resposta de mensagem de sucesso."""

    message: str
