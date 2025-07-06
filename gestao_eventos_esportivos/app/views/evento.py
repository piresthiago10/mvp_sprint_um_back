from flask_openapi3 import Tag
from flask_openapi3.blueprint import APIBlueprint

from app.schemas.evento import (
    SuccessMessage,
    EventoPath,
    EventoBase,
    EventoCriacaoResponse,
    EventoListagemResponse
    )
from app.schemas.error import ErrorSchema

from app.models.evento import Evento as evento_model
from app.models.endereco import Endereco as endereco_model
from app.models.trajeto import Trajeto as trajeto_model

from app.services.evento import Evento as evento_service
from app.services.endereco import Endereco as endereco_service
from app.services.trajeto import Trajeto as trajeto_service

from app.models import Session

db_session = Session()

# Tag de documentação
evento_tag = Tag(name="Evento", description="Endpoint de evento")

# Criação do blueprint
evento_bp = APIBlueprint(
    "Evento", __name__, url_prefix="/evento", abp_tags=[evento_tag]
)


@evento_bp.post("", responses={201: EventoCriacaoResponse, 400: ErrorSchema})
def post_evento(body: EventoBase):
    """Cria um novo evento."""
    try:
        data = body.model_dump()
        endereco_svc = endereco_service(db_session, endereco_model)
        trajeto_svc = trajeto_service(db_session, trajeto_model)
        evento_svc = evento_service(db_session, evento_model)

        data = {
            "nome": data["nome"],
            "data": data["data"],
            "endereco_id": endereco_svc.criar(data["endereco"]),
            "trajeto_id": trajeto_svc.criar(data["trajeto"]),
        }

        id_evento = evento_svc.criar(data)
        return {"id": id_evento}, 201
    except Exception as e:
        return {"message": str(e)}, 400

@evento_bp.get("/todos", responses={200: EventoListagemResponse})
def get_evento():
    """Listar todos os eventos."""
    evento_svc = evento_service(db_session, evento_model)
    return {"eventos": evento_svc.listar()}, 200

@evento_bp.get("/<int:id>", responses={200: EventoBase, 400: ErrorSchema})
def get_evento_completo(path: EventoPath):
    """Listar um evento por id."""
    try:
        evento_svc = evento_service(db_session, evento_model)
        return evento_svc.obter_evento_completo(path.id), 200
    except Exception as e:
        return {"message": str(e)}, 400
    
@evento_bp.put("/<int:id>", responses={200: SuccessMessage, 400: ErrorSchema})
def altera_evento_completo(path: EventoPath, body: EventoBase):
    """Altera um evento."""
    try:
        data = body.model_dump()
        trajeto_svc = trajeto_service(db_session, trajeto_model)
        evento_svc = evento_service(db_session, evento_model)
        endereco_svc = endereco_service(db_session, endereco_model)
        evento_completo = evento_svc.obter_evento_completo(path.id)
        
        endereco_svc.editar(evento_completo["endereco"]["id"], data["endereco"])
        trajeto_svc.editar(evento_completo["trajeto"]["id"], data["trajeto"])
        evento_svc.editar(path.id, {"nome": data["nome"], "data": data["data"]})
        return {"message": "Evento alterado com sucesso"}, 200
    except Exception as e:
        return {"message": str(e)}, 400
    
@evento_bp.delete("/<int:id>", responses={200: SuccessMessage, 400: ErrorSchema})
def excluir_evento(path: EventoPath):
    """Excluir evento."""
    try:
        evento_svc = evento_service(db_session, evento_model)
        evento_svc.deletar(path.id)
        return {"message": "Evento excluido com sucesso"}, 200
    except Exception as e:
        return {"message": str(e)}, 400