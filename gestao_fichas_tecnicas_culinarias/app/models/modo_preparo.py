from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class ModoPreparo(Base):
    """Tabela ModoPreparo."""

    __tablename__ = "modo_preparo"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    instrucao: Mapped[str] = mapped_column(nullable=False)
    ficha_tecnica: Mapped[int] = relationship("FichaTecnica")
