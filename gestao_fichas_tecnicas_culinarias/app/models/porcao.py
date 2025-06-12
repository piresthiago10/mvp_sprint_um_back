from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Porcao(Base):
    """Tabela Porcao."""

    __tablename__ = "porcao"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    validade: Mapped[str] = mapped_column(nullable=False)
    preso: Mapped[str] = mapped_column(nullable=False)
    ficha_tecnica: Mapped[int] = relationship("FichaTecnica")
