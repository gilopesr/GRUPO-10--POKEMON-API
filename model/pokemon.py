from config import db

pokemon_habilidade = db.Table(
    "pokemon_habilidade",
    db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id"), primary_key=True),
    db.Column("habilidade_id", db.Integer, db.ForeignKey("habilidade.id"), primary_key=True),
)

class Pokemon(db.Model):
    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey("tipo.id"))
    
    tipo = db.relationship("Tipo", backref="pokemons")
    habilidades = db.relationship(
        "Habilidade",
        secondary=pokemon_habilidade,
        backref="pokemons",
        lazy="joined",
    )
    
    evolucoes_de = db.relationship("Evolucao", foreign_keys="Evolucao.de_pokemon_id", back_populates="de_pokemon")
    evolucoes_para = db.relationship("Evolucao", foreign_keys="Evolucao.para_pokemon_id", back_populates="para_pokemon")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "altura": self.altura,
            "peso": self.peso,
            "tipo_id": self.tipo_id,
            "tipo": self.tipo.nome if self.tipo else None,
            "habilidades": [h.to_dict() for h in self.habilidades],
            "evolucoes": [
                {
                    "id": evo.id,
                    "para_pokemon_id": evo.para_pokemon_id,
                    "para_pokemon": evo.para_pokemon.nome if evo.para_pokemon else None,
                    "condicao": evo.condicao,
                    "habilidade": evo.habilidade,
                }
                for evo in self.evolucoes_de
            ],
        }