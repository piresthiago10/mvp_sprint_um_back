from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.models.base import Base


class Endereco(Base):
    """Model de Endereco."""

    __tablename__ = "endereco"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    logradouro: Mapped[str] = mapped_column(String(100), nullable=False)
    numero: Mapped[str] = mapped_column(String(10), nullable=False)
    complemento: Mapped[str] = mapped_column(String(50), nullable=True)
    bairro: Mapped[str] = mapped_column(String(50), nullable=False)
    cidade: Mapped[str] = mapped_column(String(50), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)
    cep: Mapped[str] = mapped_column(String(10), nullable=False)
