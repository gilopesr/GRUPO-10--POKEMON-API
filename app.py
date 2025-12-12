from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
from config import app, db

from controller.pokemon_controller import pokemon_bp
from controller.habilidade_controller import habilidade_bp
from controller.evolucao_controller import evolucao_bp
from controller.tipo_controller import tipo_bp

swagger = Swagger(app)

app.register_blueprint(pokemon_bp, url_prefix='/api/pokemons')
app.register_blueprint(habilidade_bp, url_prefix='/api/habilidades')
app.register_blueprint(evolucao_bp, url_prefix='/api/evolucoes')
app.register_blueprint(tipo_bp, url_prefix='/api/tipos')

@app.route('/')
def home():
    """
    Página inicial da API
    ---
    responses:
      200:
        description: API Pokémon Online
    """
    return jsonify({
        "message": "Bem-vindo à API Pokémon!",
        "version": "1.0.0",
        "endpoints": {
            "pokemons": "/api/pokemons",
            "habilidades": "/api/habilidades", 
            "evolucoes": "/api/evolucoes",
            "tipos": "/api/tipos",
            "documentacao": "/apidocs"
        }
    })

@app.route('/health')
def health_check():
    """
    Verificar status da API
    ---
    responses:
      200:
        description: API está funcionando
    """
    return jsonify({"status": "healthy", "message": "API Pokémon está online"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint não encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Tabelas do banco de dados criadas com sucesso!")
        print("🚀 Servidor pronto para iniciar...")
        print("📚 Documentação disponível em: http://localhost:5000/apidocs")
    
    app.run(
        host=app.config["HOST"], 
        port=app.config['PORT'], 
        debug=app.config['DEBUG']
    )
