from flask import request, jsonify
from model import db
from model.habilidade import Habilidade

class HabilidadeController:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

        habilidade = Habilidade(nome=str(data["nome"]).strip(), descricao=data.get("descricao"))
        db.session.add(habilidade)
        db.session.commit()
        return jsonify({"message": "Habilidade criada com sucesso!", "habilidade": habilidade.to_dict()}), 201

    @staticmethod
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
        if "nome" in data: habilidade.nome = str(data["nome"]).strip() or habilidade.nome
        if "descricao" in data: habilidade.descricao = data["descricao"]

        db.session.commit()
        return jsonify({"message": "Habilidade atualizada com sucesso!", "habilidade": habilidade.to_dict()}), 200

    @staticmethod
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
        db.session.delete(habilidade)
        db.session.commit()
        return jsonify({"message": "Habilidade excluída com sucesso!"}), 200
