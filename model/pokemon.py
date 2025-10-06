from config import db

class Pokemon(db.Model):
    tablename = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey("tipo.id"))
    tipo = db.relationship("Tipo", backref="pokemons")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "altura": self.altura,
            "peso": self.peso,
            "tipo_id": self.tipo_id,
            "tipo": self.tipo.nome if self.tipo else None
        }
