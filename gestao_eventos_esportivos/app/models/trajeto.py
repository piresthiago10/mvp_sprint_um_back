from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from app.models import Base
from app.models.evento import Evento


class Trajeto(Base):
    """Model de Trajeto."""

    __tablename__ = "trajeto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    nivel_dificuldade: Mapped[str] = mapped_column(String(50), nullable=False)
    altimetria: Mapped[float] = mapped_column(nullable=False)
    rota_imagem_link: Mapped[str] = mapped_column(String(255), nullable=True)
