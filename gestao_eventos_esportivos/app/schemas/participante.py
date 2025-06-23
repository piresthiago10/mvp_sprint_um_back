from pydantic import BaseModel, Field, constr
from typing import Annotated
from datetime import date

from schemas import EnderecoBase


class ParticipanteBase(BaseModel):
    """Define como um participante será representado."""

    nome: str = Field(
        description="Nome do participante", example="Joaquim", max_length=100
    )
    sobrenome: str = Field(
        description="Sobrenome do participante", example="Silva", max_length=100
    )
    cpf: str = Field(
        description="Cpf do participante",
        example="12345678901",
        min_length=11,
        max_length=11,
    )
    data_nascimento: date = Field(
        description="Data de nascimento do participante", example="1999-01-01"
    )
    endereco: EnderecoBase = Field(description="Endereco do participante")
