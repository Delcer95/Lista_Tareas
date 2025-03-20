from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    completada = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Tarea {self.descripcion}>'
