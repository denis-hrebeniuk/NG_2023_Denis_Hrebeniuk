from app import app, auth, db
from app.models import Messages, Users
from flask import request
from os import environ

import jwt
import json

SECRET_JWT_KEY = environ.get("SECRET_JWT_KEY")


def send_error(error):
    return json.dumps({"error": error})


@auth.verify_token
def verify_token(token):
    user = Users.query.where(Users.jwt_token == token).first()
    if user is not None:
        return user.id

    return False


@app.route("/api/register", methods=["POST"])
def register():
    data = request.json

    if "login" not in data or "password" not in data:
        return send_error(
            "Please, pass all expected arguments (login, password and password confirmation)"
        )

    login = data["login"]
    password = data["password"]

    if Users.query.where(Users.login == login).all():
        return send_error("The login you passed is already taken")

    token = jwt.encode({"login": login}, SECRET_JWT_KEY, algorithm="HS256")

    db.session.add(Users(login=login, password=password, jwt_token=token))
    db.session.commit()

    return json.dumps({"token": token})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json

    if "login" not in data or "password" not in data:
        return send_error("Please, pass all expected arguments (login and password)")

    login = data["login"]
    password = data["password"]

    user = Users.query.where(Users.login == login).first()
    if user is not None:
        if user.password == password:
            return json.dumps({"token": user.jwt_token})

    return send_error("Invalid login or password")


@app.route("/api/send-message", methods=["POST"])
@auth.login_required
def send():
    data = request.json

    if "message" not in data:
        return send_error("Please, pass message to send")

    message = data["message"]

    db.session.add(Messages(user_id=auth.current_user(), message=message))
    db.session.commit()

    return json.dumps({"status": "OK"})


@app.route("/api/get-messages", methods=["GET"])
@auth.login_required
def all():
    messages = []

    for message in Messages.query.all():
        user = Users.query.filter(Users.id == message.user_id).first()
        messages.append(
            {
                "sender": user.login,
                "message": message.message,
                "messageDate": str(message.message_date),
            }
        )

    if not messages:
        return send_error("Messages not found")

    return json.dumps(messages)


@app.route("/")
def index():
    return "API works"
