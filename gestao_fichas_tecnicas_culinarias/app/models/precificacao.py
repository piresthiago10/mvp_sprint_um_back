from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Precificacao(Base):
    """Tabela Precificação."""

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    custo: Mapped[float] = mapped_column(nullable=False)
    lucratividade: Mapped[float] = mapped_column(nullable=False)
    preco_praticado: Mapped[float] = mapped_column(nullable=False)
    preco_sugerido: Mapped[float] = mapped_column(nullable=False)
    porcao: Mapped[int] = relationship("Porcao")
