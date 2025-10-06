from config import db

TIPOS_VALIDOS = [
    "Normal", "Fogo", "Água", "Planta", "Elétrico", "Gelo", "Lutador", "Veneno",
    "Terra", "Voador", "Psíquico", "Inseto", "Pedra", "Fantasma", "Dragão", "Sombrio"
]

class Tipo(db.Model):
    __tablename__ = "tipo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    vantagem = db.Column(db.String(50))
    fraqueza = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "vantagem": self.vantagem,
            "fraqueza": self.fraqueza
        }

    @staticmethod
    def tipos_validos():
        """Retorna a lista de tipos pré-definidos"""
        return TIPOS_VALIDOS
