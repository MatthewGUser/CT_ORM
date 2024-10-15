from connect_to_db import db

class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    workout_sessions = db.relationship('WorkoutSession', backref='member', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email
