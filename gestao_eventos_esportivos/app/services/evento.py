from sqlalchemy.orm import Session, joinedload
from app.models.evento import Evento as evento_model


class Evento:
    """Define um evento."""

    def __init__(
        self,
        data_base: Session,
        model: evento_model,
    ):
        self.db = data_base
        self.model = model

    def criar(self, data: dict) -> evento_model:
        """Criar um novo evento."""
        evento = self.model(**data)
        self.db.add(evento)
        self.db.commit()
        self.db.refresh(evento)
        return evento

    def listar(self) -> list[evento_model]:
        """Listar todos os eventos."""
        results = self.db.query(self.model).all()
        return [item.__dict__ for item in results]

    def obter_evento_completo(self, id: int) -> evento_model:
        """Obtem evento com todos os dados incluindo trajeto e endereço."""
        result = (
            self.db.query(self.model)
            .options(joinedload(self.model.trajeto), joinedload(self.model.endereco))
            .filter(self.model.id == id)
            .first()
        )
        return self.__to_dict(result)

    def editar(self, id: int, data: dict) -> evento_model:
        """Editar um evento."""
        return self.db.query(self.model).filter(self.model.id == id).update(data)

    def deletar(self, id: int) -> None:
        """Deletar um evento."""
        return self.db.query(self.model).filter(self.model.id == id).delete()

    def __to_dict(self, result):
        """Converte o objeto para um dicionário."""
        return {
            "id": result.id,
            "nome": result.nome,
            "data": result.data.strftime('%d/%m/%Y'),
            "endereco": {
                "id": result.endereco.id,
                "logradouro": result.endereco.logradouro,
                "numero": result.endereco.numero,
                "complemento": result.endereco.complemento,
                "bairro": result.endereco.bairro,
                "cidade": result.endereco.cidade,
                "estado": result.endereco.estado,
                "cep": result.endereco.cep
                         },
            "trajeto": {
                "id": result.trajeto.id,
                "nome": result.trajeto.nome,
                "nivel_dificuldade": result.trajeto.nivel_dificuldade,
                "altimetria": result.trajeto.altimetria,
                "rota_imagem_link": result.trajeto.rota_imagem_link
            }
        }