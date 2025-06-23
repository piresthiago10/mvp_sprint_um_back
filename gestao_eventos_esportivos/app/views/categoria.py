from flask_openapi3 import Tag
from flask_openapi3.blueprint import APIBlueprint
from pydantic import BaseModel

from app.schemas import GetCategoriasSchema, ErrorSchema

# Tag de documentação
categoria_tag = Tag(name="Categoria", description="Endpoint de categoria")

# Criação do blueprint
categoria_bp = APIBlueprint(
    "Categoria", __name__, url_prefix="/categoria", abp_tags=[categoria_tag]
)


@categoria_bp.get("/categorias", responses={200: GetCategoriasSchema, 404: ErrorSchema})
def get_categorias():
    return {"message": "Teste"}
