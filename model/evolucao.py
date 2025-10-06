from config import db

class Evolucao(db.Model):
    __tablename__ = "evolucao"

    id = db.Column(db.Integer, primary_key=True)

    de_pokemon_id   = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    para_pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)

    condicao  = db.Column(db.String(100))
    habilidade = db.Column(db.String(100)) 

    de_pokemon   = db.relationship("Pokemon", foreign_keys=[de_pokemon_id], back_populates="evolucoes_de")
    para_pokemon = db.relationship("Pokemon", foreign_keys=[para_pokemon_id], back_populates="evolucoes_para")

    def to_dict(self):
        return {
            "id": self.id,
            "de_pokemon_id": self.de_pokemon_id,
            "de_pokemon": self.de_pokemon.nome if self.de_pokemon else None,
            "para_pokemon_id": self.para_pokemon_id,
            "para_pokemon": self.para_pokemon.nome if self.para_pokemon else None,
            "condicao": self.condicao,
            "habilidade": self.habilidade,
        }