import pytest
from datetime import date
from app.services.evento import Evento as evento_service
from app.services.trajeto import Trajeto as trajeto_service
from app.services.endereco import Endereco as endereco_service
from app.models.evento import Evento as evento_model
from app.models.endereco import Endereco as endereco_model
from app.models.trajeto import Trajeto as trajeto_model
from app.tests.fixtures.endereco import endereco_in_db
from app.tests.fixtures.trajeto import trajeto_in_db
from app.tests.fixtures.evento import evento_in_db


def test_criar_evento(test_db_session, endereco_in_db, trajeto_in_db):
    """Testa a criação de um evento com dados do trajeto e endereco."""

    endereco_svc = endereco_service(test_db_session, endereco_model)
    trajeto_svc = trajeto_service(test_db_session, trajeto_model)

    enderecos = endereco_svc.listar()
    trajetos = trajeto_svc.listar()

    service = evento_service(test_db_session, evento_model)
    data = {
        "nome": "Evento Teste",
        "data": date(2025, 7, 1),
        "endereco_id": enderecos[0].id,
        "trajeto_id": trajetos[0].id,
    }

    result = service.criar(data)
    assert result


def test_listar_eventos(test_db_session, evento_in_db):
    """Testa a listagem de eventos."""
    with test_db_session.no_autoflush:
        service = evento_service(test_db_session, evento_model)
        result = service.listar()
        assert result


def test_obter_evento_completo(
    test_db_session, evento_in_db, endereco_in_db, trajeto_in_db
):
    """Testa a listagem de um evento por id."""
    with test_db_session.no_autoflush:
        service = evento_service(test_db_session, evento_model)
        eventos = service.listar()
        result = service.obter_evento_completo(eventos[0]["id"])
        assert result


def test_editar_evento(test_db_session, evento_in_db):
    """Testa a edição de um evento."""

    with test_db_session.no_autoflush:
        service = evento_service(test_db_session, evento_model)
        eventos = service.listar()
        data = {"nome": "Evento Editado", "data": date(2025, 7, 1)}

        result = service.editar(eventos[0]["id"], data)
        assert result


def test_excluir_evento(test_db_session, evento_in_db):
    """Testa a exclusão de um evento."""

    with test_db_session.no_autoflush:
        service = evento_service(test_db_session, evento_model)
        eventos = service.listar()

        result = service.deletar(eventos[0]["id"])
        assert result
