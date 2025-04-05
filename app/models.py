# Defines database models

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Habit class in database
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    streak = db.Column(db.Integer, default=0)
    last_completed = db.Column(db.Date)