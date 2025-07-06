import pytest
from unittest import mock
from main import app
from app.tests.mocks.evento import (
    EVENTO_COMPLETO_PAYLOAD,
    EVENTO_COMPLETO_UPDATE_PAYLOAD
    )


def test_criar_evento():
    """Testa a criação de um novo evento."""
    data = 1

    with mock.patch("app.services.evento.Evento.criar") as evento_mock:
        with mock.patch("app.services.trajeto.Trajeto.criar") as trajeto_mock:
            with mock.patch("app.services.endereco.Endereco.criar") as endereco_mock:
                evento_mock.return_value = data
                trajeto_mock.return_value = data
                endereco_mock.return_value = data

                with app.test_client() as client:
                    response = client.post(
                        "/evento", json=EVENTO_COMPLETO_PAYLOAD)
                    assert response.status_code == 201
                    assert response.get_json() == {"id": data}

                    trajeto_mock.side_effect = Exception(
                        "Erro ao criar a evento")
                    response = client.post(
                        "/evento", json=EVENTO_COMPLETO_PAYLOAD)
                    assert response.status_code == 400
                    assert response.get_json() == {
                        "message": "Erro ao criar a evento"}


def test_listar_eventos():
    """Testa a listagem de eventos."""
    with mock.patch("app.services.evento.Evento.listar") as listar_mock:
        listar_mock.return_value = [
            {"id": 1, "nome": "Evento 1"}, {"id": 2, "nome": "Evento 2"}]
        with app.test_client() as client:
            response = client.get("/evento/todos")
            assert response.status_code == 200
            assert response.get_json() == {
                "eventos": [{"id": 1, "nome": "Evento 1"}, {"id": 2, "nome": "Evento 2"}]
            }

def test_get_evento_completo():
    """Testa a representação de um evento por id."""
    with mock.patch("app.services.evento.Evento.obter_evento_completo") as obter_mock:
        obter_mock.return_value = {"id": 1, "nome": "Evento 1"}
        with app.test_client() as client:
            response = client.get("/evento/1")
            assert response.status_code == 200
            assert response.get_json() == {"id": 1, "nome": "Evento 1"}
            
def test_altera_evento_completo():
    """Testa a alteração de um evento por completo."""
    with mock.patch("app.services.evento.Evento.editar") as evento_mock:
        with mock.patch("app.services.trajeto.Trajeto.editar") as trajeto_mock:
            with mock.patch("app.services.endereco.Endereco.editar") as endereco_mock:
                evento_mock.return_value = True
                trajeto_mock.return_value = True
                endereco_mock.return_value = True
                with app.test_client() as client:
                    response = client.put("/evento/1", json=EVENTO_COMPLETO_UPDATE_PAYLOAD)
                    assert response.status_code == 200
                    
def test_excluir_evento():
    """Testa a exclusão de um evento."""
    with mock.patch("app.services.evento.Evento.deletar") as deletar_mock:
        deletar_mock.return_value = True
        with app.test_client() as client:
            response = client.delete("/evento/1")
            assert response.status_code == 200