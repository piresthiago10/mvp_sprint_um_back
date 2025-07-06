from datetime import date

EVENTO_COMPLETO_PAYLOAD = {
    "data": "2025-10-01",
    "endereco": {
        "bairro": "Centro",
        "cep": "12345678",
        "cidade": "Rio de Janeiro",
        "complemento": "Praça",
        "estado": "RJ",
        "logradouro": "logradouro 1",
        "numero": "123",
    },
    "nome": "Evento Teste",
    "trajeto": {
        "altimetria": 600.0,
        "nivel_dificuldade": "Facil",
        "nome": "Trajeto 1",
        "rota_imagem_link": "https://example.com/rota1.jpg",
    },
}

EVENTO_COMPLETO_UPDATE_PAYLOAD = {
    "data": "2025-10-01",
    "endereco": {
        "bairro": "Centro",
        "cep": "12345678",
        "cidade": "Rio de Janeiro",
        "complemento": "Praça",
        "estado": "RJ",
        "logradouro": "logradouro 1",
        "numero": "123",
    },
    "nome": "Evento Teste",
    "trajeto": {
        "altimetria": 600.0,
        "nivel_dificuldade": "Facil",
        "nome": "Trajeto 1",
        "rota_imagem_link": "https://example.com/rota1.jpg",
    },
}
