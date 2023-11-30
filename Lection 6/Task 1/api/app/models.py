from app import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(256))
    jwt_token = db.Column(db.String(256))


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    message = db.Column(db.String(256))
    message_date = db.Column(db.DateTime, default=datetime.now)
