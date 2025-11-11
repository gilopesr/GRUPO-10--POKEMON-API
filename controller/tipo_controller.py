from flask import Blueprint, request, jsonify
from config import db
from model.tipo import Tipo, TIPOS_VALIDOS

tipo_bp = Blueprint('tipo', __name__)

@tipo_bp.route('/', methods=['GET'])
def list_tipos():
    """
    Listar tipos
    ---
    tags:
      - Tipos
    responses:
      200:
        description: Lista de tipos
    """
    tipos = Tipo.query.all()
    return jsonify([tipo.to_dict() for tipo in tipos]), 200

@tipo_bp.route('/<int:tipo_id>', methods=['GET'])
def get_tipo(tipo_id):
    """
    Obter tipo
    ---
    tags:
      - Tipos
    parameters:
      - name: tipo_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """
    tipo = Tipo.query.get(tipo_id)
    if not tipo:
        return jsonify({"error": "Tipo não encontrado"}), 404
    return jsonify(tipo.to_dict()), 200

@tipo_bp.route('/', methods=['POST'])
def create_tipo():
    """
    Criar tipo
    ---
    tags:
      - Tipos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nome]
          properties:
            nome: {type: string, example: "Fogo"}
            vantagem: {type: string, example: "Planta"}
            fraqueza: {type: string, example: "Água"}
    responses:
      201:
        description: Criado
    """
    data = request.get_json()
    if not data or "nome" not in data:
        return jsonify({"error": "Campo obrigatório: nome"}), 400

    nome = str(data["nome"]).strip().capitalize()
    if nome not in TIPOS_VALIDOS:
        return jsonify({
            "error": f"Tipo inválido. Use apenas um dos seguintes: {', '.join(TIPOS_VALIDOS)}"
        }), 400

    tipo = Tipo(
        nome=nome, 
        vantagem=data.get("vantagem"), 
        fraqueza=data.get("fraqueza")
    )
    
    try:
        db.session.add(tipo)
        db.session.commit()
        return jsonify({"message": "Tipo criado com sucesso!", "tipo": tipo.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao criar tipo"}), 500

@tipo_bp.route('/<int:tipo_id>', methods=['PUT'])
def update_tipo(tipo_id):
    """
    Atualizar tipo
    ---
    tags:
      - Tipos
    parameters:
      - name: tipo_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            vantagem: {type: string}
            fraqueza: {type: string}
    responses:
      200:
        description: Atualizado
      404:
        description: Não encontrado
    """
    tipo = Tipo.query.get(tipo_id)
    if not tipo:
        return jsonify({"error": "Tipo não encontrado"}), 404

    data = request.get_json() or {}
    
    if "vantagem" in data:
        tipo.vantagem = data["vantagem"]
    if "fraqueza" in data:
        tipo.fraqueza = data["fraqueza"]

    try:
        db.session.commit()
        return jsonify({"message": "Tipo atualizado com sucesso!", "tipo": tipo.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar tipo"}), 500

@tipo_bp.route('/<int:tipo_id>', methods=['DELETE'])
def delete_tipo(tipo_id):
    """
    Excluir tipo
    ---
    tags:
      - Tipos
    parameters:
      - name: tipo_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Excluído
      404:
        description: Não encontrado
    """
    tipo = Tipo.query.get(tipo_id)
    if not tipo:
        return jsonify({"error": "Tipo não encontrado"}), 404
    
    try:
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({"message": "Tipo excluído com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao excluir tipo"}), 500

@tipo_bp.route('/validos', methods=['GET'])
def list_tipos_validos():
    """
    Listar tipos válidos
    ---
    tags:
      - Tipos
    responses:
      200:
        description: Lista de tipos pré-definidos
    """
    return jsonify({"tipos_validos": TIPOS_VALIDOS}), 200