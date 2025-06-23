import pytest
import json
from sqlalchemy.orm import Session
from datetime import date
from app.services.participante import Participante as participante_service
from app.services.endereco import Endereco as endereco_service
from app.models.participante import Participante as participante_model
from app.models.endereco import Endereco as endereco_model
from app.tests.fixtures.participante import participante_in_db
from app.tests.fixtures.endereco import endereco_in_db


def test_criar_participante(db_session, endereco_in_db):
    """Testa a criação de um participante com dados do endereco."""

    service = participante_service(db_session, participante_model)
    enderecos = endereco_service(db_session, endereco_model).listar()

    data = {
        "nome": "Maria",
        "sobrenome": "Silva",
        "cpf": "12345678901",
        "data_nascimento": date(1990, 1, 1),
        "endereco_id": enderecos[0].id,
    }

    result = service.criar(data)
    assert result
    
def test_listar_participantes(db_session, participante_in_db):
    """Testa a listagem de participantes."""

    service = participante_service(db_session, participante_model)
    result = service.listar()
    assert result
    
def test_obter_participante_completo(db_session, participante_in_db, endereco_in_db):
    """Testa a listagem de um participante por id."""

    service = participante_service(db_session, participante_model)
    participantes = service.listar()
    result = service.obter_participante_completo(participantes[0]["id"])
    assert result
    
def test_editar_participante(db_session, participante_in_db):
    """Testa a edição de um participante."""

    service = participante_service(db_session, participante_model)
    participantes = service.listar()
    data = {
        "nome": "Maria",
        "sobrenome": "Silva",
        "cpf": "12345678901",
        "data_nascimento": date(1990, 1, 1),
    }

    result = service.editar(participantes[0]["id"], data)
    assert result
    
def test_excluir_participante(db_session, participante_in_db):
    """Testa a exclusão de um participante."""

    service = participante_service(db_session, participante_model)
    participantes = service.listar()

    result = service.deletar(participantes[0]["id"])
    assert result