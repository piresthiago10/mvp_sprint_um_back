from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TrajetoBase(BaseModel):
    """Define como um trajeto será representado."""

    nome: str = Field(description="Nome do trajeto", example="Caminhada pela saúde", max_length=140)
    nivel_dificuldade: str = Field(description="Nivel de dificuldade do trajeto", example="Facil")
    altimetria: float = Field(description="Altimetria do trajeto", example=600.0)
    rota_imagem_link: Optional[str] = Field(
        description="Link da imagem da rota", example="https://example.com/rota1.jpg")

    model_config = ConfigDict(from_attributes=True)

