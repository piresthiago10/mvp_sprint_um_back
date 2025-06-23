import pytest
from datetime import date
from sqlalchemy.orm import Session
from app.models.participante import Participante


@pytest.fixture(scope="function")
def participante_in_db(db_session: Session):
    """Fixture para criar três participantes no banco de dados para os testes."""

    participantes = [
        Participante(
            nome="Maria",
            sobrenome="Silva",
            cpf="12345678901",
            data_nascimento=date(1990, 1, 1),
            endereco_id=1
        ),
        Participante(
            nome="João",
            sobrenome="Moraes",
            cpf="12345678902",
            data_nascimento=date(1991, 2, 1),
            endereco_id=2
        ),
        Participante(
            nome="Pedro",
            sobrenome="Santos",
            cpf="12345678903",
            data_nascimento=date(1992, 3, 1),
            endereco_id=3
        ),
    ]

    with db_session.begin():
        db_session.add_all(participantes)
    db_session.commit()

    return participantes
