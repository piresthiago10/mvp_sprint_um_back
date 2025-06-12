from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Insumo(Base):
    """Tabela Insumo."""

    __tablename__ = "insumo"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    ingreditente: Mapped[str] = mapped_column(nullable=False)
    unidade: Mapped[str] = mapped_column(nullable=False)
    quantidade_bruta: Mapped[float] = mapped_column(nullable=False)
    quantidade_liquida: Mapped[float] = mapped_column(nullable=False)
    fator_correcao: Mapped[float] = mapped_column(nullable=False)
    custo_unitario: Mapped[float] = mapped_column(nullable=False)
    custo_total: Mapped[float] = mapped_column(nullable=False)
    ficha_tecnica: Mapped[int] = relationship("FichaTecnica")
