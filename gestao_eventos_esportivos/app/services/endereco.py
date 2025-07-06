from sqlalchemy.orm import Session
from app.models.endereco import Endereco as endereco_model


class Endereco:
    def __init__(self, data_base: Session, model: endereco_model):
        self.db = data_base
        self.model = model

    def criar(self, data: dict) -> endereco_model:
        """Criar um novo endereco."""
        endereco = self.model(**data)
        self.db.add(endereco)
        self.db.commit()
        self.db.refresh(endereco)
        return endereco.id

    def listar(self) -> list[endereco_model]:
        """Listar todos os enderecos."""
        return self.db.query(self.model).all()

    def listar_por_id(self, id: int) -> endereco_model:
        """Listar um endereco por id."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def editar(self, id: int, data: dict) -> endereco_model:
        """Editar um endereco."""
        return self.db.query(self.model).filter(self.model.id == id).update(data)

    def deletar(self, id: int) -> None:
        """Deletar um endereco."""
        return self.db.query(self.model).filter(self.model.id == id).delete()
