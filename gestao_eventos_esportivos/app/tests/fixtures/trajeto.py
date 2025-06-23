import pytest
from sqlalchemy.orm import Session
from app.models.trajeto import Trajeto


@pytest.fixture(scope="function")
def trajeto_in_db(db_session: Session):
    """Fixture para criar três trajetos no banco de dados para os testes."""
    trajetos = [
        Trajeto(
            nome="Trajeto 1",
            nivel_dificuldade="Facil",
            altimetria=600.0,
            rota_imagem_link="https://example.com/rota1.jpg",
        ),
        Trajeto(
            nome="Trajeto 2",
            nivel_dificuldade="Médio",
            altimetria=1.470,
            rota_imagem_link="https://example.com/rota2.jpg",
        ),
        Trajeto(
            nome="Trajeto 3",
            nivel_dificuldade="Dificil",
            altimetria=2.367,
            rota_imagem_link="https://example.com/rota3.jpg",
        ),
    ]

    with db_session.begin():
        db_session.add_all(trajetos)
    db_session.commit()

    return trajetos
