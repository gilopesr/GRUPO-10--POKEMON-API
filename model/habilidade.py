from config import db

class Habilidade(db.Model):
    __tablename__ = "habilidades"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable=False)
    força = db.Column(db.Integer,nullable=False)