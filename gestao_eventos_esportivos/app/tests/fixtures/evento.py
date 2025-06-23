import pytest
from datetime import date
from sqlalchemy.orm import Session
from app.models.evento import Evento


@pytest.fixture(scope="function")
def evento_in_db(db_session: Session):
    """Fixture para criar três eventos no banco de dados para os testes."""

    eventos = [
        Evento(
            nome="Evento 1",
            data=date(2023, 1, 1),
            endereco_id=1,
            trajeto_id=1,
        ),
        Evento(
            nome="Evento 2",
            data=date(2023, 2, 1),
            endereco_id=2,
            trajeto_id=2,
        ),
        Evento(
            nome="Evento 3",
            data=date(2023, 3, 1),
            endereco_id=3,
            trajeto_id=3,
        ),
    ]

    with db_session.begin():
        db_session.add_all(eventos)
    db_session.commit()

    return eventos
