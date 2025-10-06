from flask import Blueprint, request, jsonify
from config import db
from model.habilidade import Habilidade

habilidade_bp = Blueprint('habilidade', __name__)

@habilidade_bp.route('/', methods=['GET'])
def list_habilidades():
    """
    Listar habilidades
    ---
    tags:
      - Habilidades
    responses:
      200:
        description: Lista de habilidades
    """
    habilidades = Habilidade.query.all()
    return jsonify([habilidade.to_dict() for habilidade in habilidades]), 200

@habilidade_bp.route('/<int:habilidade_id>', methods=['GET'])
def get_habilidade(habilidade_id):
    """
    Obter habilidade
    ---
    tags:
      - Habilidades
    parameters:
      - name: habilidade_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: OK
      404:
        description: Não encontrada
    """
    habilidade = Habilidade.query.get(habilidade_id)
    if not habilidade:
        return jsonify({"error": "Habilidade não encontrada"}), 404
    return jsonify(habilidade.to_dict()), 200

@habilidade_bp.route('/', methods=['POST'])
def create_habilidade():
    """
    Criar habilidade
    ---
    tags:
      - Habilidades
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nome]
          properties:
            nome: {type: string, example: "Jato d'Água"}
            descricao: {type: string, example: "Ataque de água de curto alcance"}
    responses:
      201:
        description: Criada
    """
    data = request.get_json()
    if not data or "nome" not in data:
        return jsonify({"error": "Campo obrigatório: nome"}), 400

    if Habilidade.query.filter_by(nome=data["nome"]).first():
        return jsonify({"error": "Já existe uma habilidade com este nome"}), 409

    habilidade = Habilidade(
        nome=str(data["nome"]).strip(), 
        descricao=data.get("descricao")
    )
    
    try:
        db.session.add(habilidade)
        db.session.commit()
        return jsonify({"message": "Habilidade criada com sucesso!", "habilidade": habilidade.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao criar habilidade"}), 500

@habilidade_bp.route('/<int:habilidade_id>', methods=['PUT'])
def update_habilidade(habilidade_id):
    """
    Atualizar habilidade
    ---
    tags:
      - Habilidades
    parameters:
      - name: habilidade_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome: {type: string}
            descricao: {type: string}
    responses:
      200:
        description: Atualizada
      404:
        description: Não encontrada
    """
    habilidade = Habilidade.query.get(habilidade_id)
    if not habilidade:
        return jsonify({"error": "Habilidade não encontrada"}), 404

    data = request.get_json() or {}
    
    if "nome" in data:
        novo_nome = str(data["nome"]).strip()
        if novo_nome and Habilidade.query.filter(Habilidade.nome == novo_nome, Habilidade.id != habilidade_id).first():
            return jsonify({"error": "Já existe uma habilidade com este nome"}), 409
        habilidade.nome = novo_nome or habilidade.nome
        
    if "descricao" in data:
        habilidade.descricao = data["descricao"]

    try:
        db.session.commit()
        return jsonify({"message": "Habilidade atualizada com sucesso!", "habilidade": habilidade.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar habilidade"}), 500

@habilidade_bp.route('/<int:habilidade_id>', methods=['DELETE'])
def delete_habilidade(habilidade_id):
    """
    Excluir habilidade
    ---
    tags:
      - Habilidades
    parameters:
      - name: habilidade_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Deletada
      404:
        description: Não encontrada
    """
    habilidade = Habilidade.query.get(habilidade_id)
    if not habilidade:
        return jsonify({"error": "Habilidade não encontrada"}), 404
    
    try:
        db.session.delete(habilidade)
        db.session.commit()
        return jsonify({"message": "Habilidade excluída com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao excluir habilidade"}), 500