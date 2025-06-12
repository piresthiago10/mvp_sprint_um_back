from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Categoria(Base):
    """Tabela Categoria."""

    __tablename__ = "categoria"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(unique=True, nullable=False)
