# Criando o servidor
from flask import Flask
# importand as rotas blueprint
from src.main.routes.trips_routes import trips_route_bp

app = Flask(__name__)

# registrando a rota
app.register_blueprint(trips_route_bp)