from ..extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks"


    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "title" : self.title,
            "description" : self.description,
            "created_at" : self.created_at
        }
