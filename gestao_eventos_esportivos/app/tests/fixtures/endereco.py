import pytest
from sqlalchemy.orm import Session
from app.models.endereco import Endereco


@pytest.fixture(scope="function")
def endereco_in_db(db_session: Session):
    """Fixture para criar três endereços no banco de dados para os testes."""
    enderecos = [
        Endereco(
            logradouro="logradouro 1",
            numero="123",
            complemento="Praça",
            bairro="Centro",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="12345678",
        ),
        Endereco(
            logradouro="logradouro 2",
            numero="456",
            complemento="Casa",
            bairro="Centro",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="12345678",
        ),
        Endereco(
            logradouro="logradouro 3",
            numero="789",
            complemento="Casa",
            bairro="Centro",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="12345678",
        ),
    ]

    with db_session.begin():
        db_session.add_all(enderecos)
    db_session.commit()

    return enderecos
