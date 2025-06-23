from sqlalchemy import Table, Column, ForeignKey
from app.models import Base

evento_participante = Table(
    "evento_participante",
    Base.metadata,
    Column("evento_id", ForeignKey("evento.id"), primary_key=True),
    Column("participante_id", ForeignKey("participante.id"), primary_key=True),
)
