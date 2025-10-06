from flask import Blueprint, request, jsonify
from config import db
from model.pokemon import Pokemon
from model.tipo import Tipo

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/', methods=['GET'])
def list_pokemons():
    """
    Listar todos os Pokémons
    ---
    tags:
      - Pokemons
    responses:
      200:
        description: Lista de pokémons
    """
    pokemons = Pokemon.query.all()
    return jsonify([pokemon.to_dict() for pokemon in pokemons]), 200

@pokemon_bp.route('/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    """
    Obter um Pokémon específico
    ---
    tags:
      - Pokemons
    parameters:
      - name: pokemon_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Pokémon encontrado
      404:
        description: Pokémon não encontrado
    """
    pokemon = Pokemon.query.get(pokemon_id)
    if not pokemon:
        return jsonify({"error": "Pokémon não encontrado"}), 404
    return jsonify(pokemon.to_dict()), 200

@pokemon_bp.route('/', methods=['POST'])
def create_pokemon():
    """
    Criar um novo Pokémon
    ---
    tags:
      - Pokemons
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nome, altura, peso, tipo_id]
          properties:
            nome: {type: string, example: "Squirtle"}
            altura: {type: integer, example: 5}
            peso: {type: integer, example: 90}
            tipo_id: {type: integer, example: 3}
    responses:
      201:
        description: Pokémon criado
    """
    data = request.get_json()

    if not data or not all(k in data for k in ("nome", "altura", "peso", "tipo_id")):
        return jsonify({"error": "Campos obrigatórios: nome, altura, peso e tipo_id"}), 400

    if Pokemon.query.filter_by(nome=data["nome"]).first():
        return jsonify({"error": "Já existe um Pokémon com esse nome"}), 409

    tipo = Tipo.query.get(data["tipo_id"])
    if not tipo:
        return jsonify({"error": "Tipo não encontrado"}), 404

    pokemon = Pokemon(
        nome=str(data["nome"]).strip(),
        altura=int(data["altura"]),
        peso=int(data["peso"]),
        tipo_id=int(data["tipo_id"])
    )

    try:
        db.session.add(pokemon)
        db.session.commit()
        return jsonify({
            "message": "Pokémon criado com sucesso!",
            "pokemon": pokemon.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao criar Pokémon"}), 500

@pokemon_bp.route('/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    """
    Atualizar um Pokémon existente
    ---
    tags:
      - Pokemons
    parameters:
      - name: pokemon_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome: {type: string}
            altura: {type: integer}
            peso: {type: integer}
            tipo_id: {type: integer}
    responses:
      200:
        description: Pokémon atualizado
      404:
        description: Pokémon não encontrado
    """
    pokemon = Pokemon.query.get(pokemon_id)
    if not pokemon:
        return jsonify({"error": "Pokémon não encontrado"}), 404

    data = request.get_json() or {}

    if "nome" in data:
        novo_nome = str(data["nome"]).strip()
        if novo_nome and Pokemon.query.filter(Pokemon.nome == novo_nome, Pokemon.id != pokemon_id).first():
            return jsonify({"error": "Já existe um Pokémon com esse nome"}), 409
        if novo_nome:
            pokemon.nome = novo_nome

    if "altura" in data:
        pokemon.altura = int(data["altura"])
    if "peso" in data:
        pokemon.peso = int(data["peso"])
    if "tipo_id" in data:
        tipo = Tipo.query.get(data["tipo_id"])
        if not tipo:
            return jsonify({"error": "Tipo não encontrado"}), 404
        pokemon.tipo_id = int(data["tipo_id"])

    try:
        db.session.commit()
        return jsonify({
            "message": "Pokémon atualizado com sucesso!",
            "pokemon": pokemon.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar Pokémon"}), 500

@pokemon_bp.route('/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    """
    Excluir um Pokémon
    ---
    tags:
      - Pokemons
    parameters:
      - name: pokemon_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Pokémon excluído
      404:
        description: Pokémon não encontrado
    """
    pokemon = Pokemon.query.get(pokemon_id)
    if not pokemon:
        return jsonify({"error": "Pokémon não encontrado"}), 404

    try:
        db.session.delete(pokemon)
        db.session.commit()
        return jsonify({"message": "Pokémon excluído com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao excluir Pokémon"}), 500