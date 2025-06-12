from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class FichaTecnica(Base):
    """Tabela FichaTecnica."""

    __tablename__ = "ficha_tecnica"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=False)
    ultima_alteracao: Mapped[str] = mapped_column(nullable=False)
    categoria: Mapped[int] = mapped_column(nullable=False)
