from flask import redirect
from flask_openapi3 import OpenAPI, Info
from app.views.evento import evento_bp
from flask_cors import CORS

info = Info(title="Gestão de Eventos Esportivos", version="1.0")
app = OpenAPI(__name__, info=info)
app.register_api(evento_bp)
CORS(app)


@app.get("/")
def docs_redirect():
    return redirect("/openapi/swagger")


if __name__ == "__main__":
    app.run(debug=True)
