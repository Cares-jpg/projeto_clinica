from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    specialty = db.Column(db.String(30))
    type = db.Column(db.String(30))
    password = db.Column(db.String(20), nullable = False)
    triage = db.Column(db.String(15))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Tarefa {repr(self.id)}>'