from pydantic import BaseModel


class TrajetoBase(BaseModel):
    """Define como um trajeto será representado."""

    nome: str
    nivel_dificuldade: str
    altimetria: float
    rota_imagem_link: str | None = None

    class Config:
        orm_mode = True