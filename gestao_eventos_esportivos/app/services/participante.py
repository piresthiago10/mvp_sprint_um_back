from sqlalchemy.orm import Session, joinedload
from app.models.participante import Participante as participante_model


class Participante:
    def __init__(self, data_base: Session, model: participante_model):
        self.db = data_base
        self.model = model

    def criar(self, data: dict) -> participante_model:
        """Criar um novo participante."""
        participante = self.model(**data)
        self.db.add(participante)
        self.db.commit()
        self.db.refresh(participante)
        return participante.id

    def listar(self) -> list[participante_model]:
        """Listar todos os participantes."""
        results = self.db.query(self.model).all()
        return [item.__dict__ for item in results]

    def obter_participante_completo(self, id: int) -> participante_model:
        """Obtem participante com todos os dados incluindo trajeto e endereço."""
        result = (
            self.db.query(self.model)
            .options(joinedload(self.model.endereco))
            .filter(self.model.id == id)
            .first()
        )
        return self.__to_dict(result)

    def editar(self, id: int, data: dict) -> participante_model:
        """Editar um participante."""
        return self.db.query(self.model).filter(self.model.id == id).update(data)

    def deletar(self, id: int) -> None:
        """Deletar um participante."""
        return self.db.query(self.model).filter(self.model.id == id).delete()

    def __to_dict(self, result):
        """Converte o objeto para um dicionário."""
        return {
            "id": result.id,
            "nome": result.nome,
            "sobrenome": result.sobrenome,
            "cpf": result.cpf,
            "data_nascimento": result.data_nascimento.strftime('%d/%m/%Y'),
            "endereco": {
                "id": result.endereco.id,
                "logradouro": result.endereco.logradouro,
                "numero": result.endereco.numero,
                "complemento": result.endereco.complemento,
                "bairro": result.endereco.bairro,
                "cidade": result.endereco.cidade,
                "estado": result.endereco.estado,
                "cep": result.endereco.cep
            }
        }
