import pytest
from sqlalchemy.orm import Session
from app.models.trajeto import Trajeto


@pytest.fixture
def trajeto_in_db(test_db_session: Session):
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

    with test_db_session.begin():
        test_db_session.add_all(trajetos)
    test_db_session.commit()

    return trajetos
