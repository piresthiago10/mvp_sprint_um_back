from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.models.base import Base

from datetime import date


class Participante(Base):
    """Model de Participante."""

    __tablename__ = "participante"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    sobrenome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), unique=True, nullable=False)
    data_nascimento: Mapped[date] = mapped_column(nullable=False)

    endereco_id: Mapped[int] = mapped_column(ForeignKey("endereco.id"), nullable=False)
    endereco = relationship("Endereco")
