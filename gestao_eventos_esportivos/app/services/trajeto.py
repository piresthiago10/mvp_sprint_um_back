from sqlalchemy.orm import Session
from app.models.trajeto import Trajeto as trajeto_model


class Trajeto:
    def __init__(self, data_base: Session, model: trajeto_model):
        self.db = data_base
        self.model = model

    def criar(self, data: dict) -> trajeto_model:
        """Criar um novo trajeto."""
        trajeto = self.model(**data)
        self.db.add(trajeto)
        self.db.commit()
        self.db.refresh(trajeto)
        return trajeto

    def listar(self) -> list[trajeto_model]:
        """Listar todos os trajetos."""
        return self.db.query(self.model).all()

    def listar_por_id(self, id: int) -> trajeto_model:
        """Listar um trajeto por id."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def editar(self, id: int, data: dict) -> trajeto_model:
        """Editar um trajeto."""
        return self.db.query(self.model).filter(self.model.id == id).update(data)

    def deletar(self, id: int) -> None:
        """Deletar um trajeto."""
        return self.db.query(self.model).filter(self.model.id == id).delete()
