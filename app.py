from flask import Flask
from flasgger import Swagger

from controller.evolucao_controller import EvolucaoController
from controller.habilidade_controller import HabilidadeController
from controller.pokemon_controller import PokemonController
from controller.tipo_controller import TipoController

from config import app, db

swagger = Swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])