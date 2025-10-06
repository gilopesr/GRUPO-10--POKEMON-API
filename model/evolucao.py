from config import db

class Evolucao(db.Model):
    tablename = "evolucao"

    id = db.Column(db.Integer, primary_key=True)
    de_pokemon = db.Column(db.String(100), nullable=False)
    para_pokemon = db.Column(db.String(100), nullable=False)
    condicao = db.Column(db.String(100))
    habilidade = db.Column(db.String(100))  # habilidade aprendida nessa evolução

    def to_dict(self):
        return {
            "id": self.id,
            "de_pokemon": self.de_pokemon,
            "para_pokemon": self.para_pokemon,
            "condicao": self.condicao,
            "habilidade": self.habilidade
        }