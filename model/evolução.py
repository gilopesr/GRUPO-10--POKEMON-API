from config import db

class Evolucao(db.Model):
    __tablename__ = "evolucao"

    id = db.Column(db.Integer, primary_key = True)
    