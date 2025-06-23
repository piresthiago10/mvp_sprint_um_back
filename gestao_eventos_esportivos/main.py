from flask import redirect
from flask_openapi3 import OpenAPI, Info
from app.views.ficha_tecnica import ficha_tecnica_bp
from app.views.categoria import categoria_bp
from flask_cors import CORS

info = Info(title="Gestão de Fichas Técnicas Culinárias", version="1.0")
app = OpenAPI(__name__, info=info)
app.register_api(ficha_tecnica_bp)
app.register_api(categoria_bp)
CORS(app)


@app.get("/")
def docs_redirect():
    return redirect("/openapi/swagger")


if __name__ == "__main__":
    app.run(debug=True)
