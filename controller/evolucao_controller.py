from flask import Blueprint, request, jsonify
from config import db
from model.evolucao import Evolucao
from model.pokemon import Pokemon

evolucao_bp = Blueprint('evolucao', __name__)

@evolucao_bp.route('/', methods=['GET'])
def list_evolucoes():
    """
    Listar evoluções
    ---
    tags:
      - Evolucoes
    responses:
      200:
        description: Lista de evoluções
    """
    evolucoes = Evolucao.query.all()
    return jsonify([evolucao.to_dict() for evolucao in evolucoes]), 200

@evolucao_bp.route('/<int:evolucao_id>', methods=['GET'])
def get_evolucao(evolucao_id):
    """
    Obter evolução
    ---
    tags:
      - Evolucoes
    parameters:
      - name: evolucao_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: OK
      404:
        description: Não encontrada
    """
    evolucao = Evolucao.query.get(evolucao_id)
    if not evolucao:
        return jsonify({"error": "Evolução não encontrada"}), 404
    return jsonify(evolucao.to_dict()), 200

@evolucao_bp.route('/', methods=['POST'])
def create_evolucao():
    """
    Criar evolução
    ---
    tags:
      - Evolucoes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [de_pokemon_id, para_pokemon_id]
          properties:
            de_pokemon_id: {type: integer, example: 1}
            para_pokemon_id: {type: integer, example: 2}
            condicao: {type: string, example: "Nível 16"}
            habilidade: {type: string, example: "Folha Navalha"}
    responses:
      201:
        description: Criada
    """
    data = request.get_json()
    if not data or not all(k in data for k in ("de_pokemon_id", "para_pokemon_id")):
        return jsonify({"error": "Campos obrigatórios: de_pokemon_id, para_pokemon_id"}), 400

    de_pokemon = Pokemon.query.get(data["de_pokemon_id"])
    para_pokemon = Pokemon.query.get(data["para_pokemon_id"])
    
    if not de_pokemon:
        return jsonify({"error": "Pokémon de origem não encontrado"}), 404
    if not para_pokemon:
        return jsonify({"error": "Pokémon de destino não encontrado"}), 404

    evolucao = Evolucao(
        de_pokemon_id=int(data["de_pokemon_id"]),
        para_pokemon_id=int(data["para_pokemon_id"]),
        condicao=data.get("condicao"),
        habilidade=data.get("habilidade"),
    )
    
    try:
        db.session.add(evolucao)
        db.session.commit()
        return jsonify({"message": "Evolução criada com sucesso!", "evolucao": evolucao.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao criar evolução"}), 500

@evolucao_bp.route('/<int:evolucao_id>', methods=['PUT'])
def update_evolucao(evolucao_id):
    """
    Atualizar evolução
    ---
    tags:
      - Evolucoes
    parameters:
      - name: evolucao_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            de_pokemon_id: {type: integer}
            para_pokemon_id: {type: integer}
            condicao: {type: string}
            habilidade: {type: string}
    responses:
      200:
        description: Atualizada
      404:
        description: Não encontrada
    """
    evolucao = Evolucao.query.get(evolucao_id)
    if not evolucao:
        return jsonify({"error": "Evolução não encontrada"}), 404

    data = request.get_json() or {}
    
    if "de_pokemon_id" in data:
        de_pokemon = Pokemon.query.get(data["de_pokemon_id"])
        if not de_pokemon:
            return jsonify({"error": "Pokémon de origem não encontrado"}), 404
        evolucao.de_pokemon_id = int(data["de_pokemon_id"])
        
    if "para_pokemon_id" in data:
        para_pokemon = Pokemon.query.get(data["para_pokemon_id"])
        if not para_pokemon:
            return jsonify({"error": "Pokémon de destino não encontrado"}), 404
        evolucao.para_pokemon_id = int(data["para_pokemon_id"])
        
    if "condicao" in data:
        evolucao.condicao = data["condicao"]
    if "habilidade" in data:
        evolucao.habilidade = data["habilidade"]

    try:
        db.session.commit()
        return jsonify({"message": "Evolução atualizada com sucesso!", "evolucao": evolucao.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar evolução"}), 500

@evolucao_bp.route('/<int:evolucao_id>', methods=['DELETE'])
def delete_evolucao(evolucao_id):
    """
    Excluir evolução
    ---
    tags:
      - Evolucoes
    parameters:
      - name: evolucao_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Deletada
      404:
        description: Não encontrada
    """
    evolucao = Evolucao.query.get(evolucao_id)
    if not evolucao:
        return jsonify({"error": "Evolução não encontrada"}), 404
    
    try:
        db.session.delete(evolucao)
        db.session.commit()
        return jsonify({"message": "Evolução excluída com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao excluir evolução"}), 500