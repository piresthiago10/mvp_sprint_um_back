from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Armazenamento(Base):
    """Tabela armazenamento"""

    __tablename__ = "armazenamento"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    embalagem: Mapped[str] = mapped_column(nullable=False)
    ambiente: Mapped[str] = mapped_column(nullable=False)
    temperatura: Mapped[str] = mapped_column(nullable=False)
    porcao: Mapped[int] = relationship("Porcao")
