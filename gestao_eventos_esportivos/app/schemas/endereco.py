from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, Field, constr


class EnderecoBase(BaseModel):
    """Define como um endereco será representado."""

    logradouro: str = Field(description="Logradouro", example="logradouro", max_length=100)
    numero: str = Field(description="Numero", example="123", max_length=10)
    complemento: str = Field(description="Complemento", exemple="Casa", max_length=50)
    bairro: str = Field(description="Bairro", example="Centro", max_length=50)
    cidade: str = Field(description="Cidade", exemple="Rio de Janeiro", max_length=50)
    estado: Annotated[str, constr(min_length=2, max_length=2)] = Field(
        description="Estado", exemple="RJ", max_length=2
    )
    cep: str = Field(description="Cep", exemple="12345678", max_length=8)

    model_config = ConfigDict(from_attributes=True)
    
class EnderecoBaseUpdate(EnderecoBase):
    """Define como um endereco será atualizado."""
    id: int = Field(description="Id do endereco", example=1)