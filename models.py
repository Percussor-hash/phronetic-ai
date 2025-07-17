from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))

    def serialize(self):
        return {"id": self.id, "content": self.content}
