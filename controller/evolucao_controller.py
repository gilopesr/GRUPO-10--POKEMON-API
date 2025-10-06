from flask import request, jsonify
from config import db
from model.evolucao import Evolucao

class EvolucaoController:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
              required: [de_pokemon, para_pokemon]
              properties:
                de_pokemon: {type: string, example: "Bulbasaur"}
                para_pokemon:{type: string, example: "Ivysaur"}
                condicao:    {type: string, example: "Nível 16"}
                habilidade:  {type: string, example: "Folha Navalha"}
        responses:
          201:
            description: Criada
        """
        data = request.get_json()
        if not data or not all(k in data for k in ("de_pokemon", "para_pokemon")):
            return jsonify({"error": "Campos obrigatórios: de_pokemon, para_pokemon"}), 400

        evolucao = Evolucao(
            de_pokemon=str(data["de_pokemon"]).strip(),
            para_pokemon=str(data["para_pokemon"]).strip(),
            condicao=data.get("condicao"),
            habilidade=data.get("habilidade"),
        )
        db.session.add(evolucao)
        db.session.commit()
        return jsonify({"message": "Evolução criada com sucesso!", "evolucao": evolucao.to_dict()}), 201

    @staticmethod
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
                de_pokemon: {type: string}
                para_pokemon:{type: string}
                condicao:    {type: string}
                habilidade:  {type: string}
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
        if "de_pokemon" in data:   evolucao.de_pokemon   = str(data["de_pokemon"]).strip() or evolucao.de_pokemon
        if "para_pokemon" in data: evolucao.para_pokemon = str(data["para_pokemon"]).strip() or evolucao.para_pokemon
        if "condicao" in data:     evolucao.condicao     = data["condicao"]
        if "habilidade" in data:   evolucao.habilidade   = data["habilidade"]

        db.session.commit()
        return jsonify({"message": "Evolução atualizada com sucesso!", "evolucao": evolucao.to_dict()}), 200

    @staticmethod
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
        db.session.delete(evolucao)
        db.session.commit()
        return jsonify({"message": "Evolução excluída com sucesso!"}), 200
