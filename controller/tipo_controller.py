from flask import request, jsonify
from config import db
from model.tipo import Tipo, TIPOS_VALIDOS

class TipoController:
    @staticmethod
    def create_tipo():
        data = request.get_json()
        if not data or "nome" not in data:
            return jsonify({"error": "Campo obrigatório: nome"}), 400

        nome = str(data["nome"]).strip().capitalize()
        if nome not in TIPOS_VALIDOS:
            return jsonify({
                "error": f"Tipo inválido. Use apenas um dos seguintes: {', '.join(TIPOS_VALIDOS)}"
            }), 400

        if Tipo.query.filter_by(nome=nome).first():
            return jsonify({"error": "Já existe um tipo com este nome"}), 409

        tipo = Tipo(nome=nome, vantagem=data.get("vantagem"), fraqueza=data.get("fraqueza"))
        db.session.add(tipo)
        db.session.commit()
        return jsonify({"message": "Tipo criado com sucesso!", "tipo": tipo.to_dict()}), 201
