from flask_openapi3 import Tag
from flask_openapi3.blueprint import APIBlueprint
from pydantic import BaseModel

# Tag de documentação
ficha_tecnica_tag = Tag(name="Ficha Tecnica", description="Endpoint de ficha técnica")

# Criação do blueprint
ficha_tecnica_bp = APIBlueprint(
    "Ficha Tecnica", __name__, url_prefix="/ficha-tecnica", abp_tags=[ficha_tecnica_tag]
)


# Modelo de entrada
class HelloInput(BaseModel):
    name: str


# Modelo de resposta
class HelloOutput(BaseModel):
    message: str


# Endpoint POST com validação
@ficha_tecnica_bp.post("", responses={200: HelloOutput})
def say_hello(body: HelloInput):
    return HelloOutput(message=f"Olá, {body.name}!")


@ficha_tecnica_bp.get("/", responses={200: HelloOutput})
def teste():
    return {"message": "Teste"}
