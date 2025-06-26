from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.models.base import Base

from datetime import date


class Evento(Base):
    """Model de Evento."""

    __tablename__ = "evento"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    data: Mapped[date] = mapped_column(nullable=False)

    trajeto_id: Mapped[int] = mapped_column(ForeignKey("trajeto.id"), nullable=False)
    endereco_id: Mapped[int] = mapped_column(ForeignKey("endereco.id"), nullable=False)

    endereco = relationship("Endereco")
    trajeto = relationship("Trajeto")
