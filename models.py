import os
from sqla_wrapper import SQLAlchemy

db = os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite").replace("postgres://", "postgresql://", 1)

SQLAlchemy(db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    secret_number = db.Column(db.Integer, unique=False)
