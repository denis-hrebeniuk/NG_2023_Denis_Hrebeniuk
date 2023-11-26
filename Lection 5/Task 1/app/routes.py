from app import app, db
from app.models import Users, Messages
from flask import request, redirect
from markupsafe import Markup


@app.route("/")
def index():
    return "Hello, app is working!"


@app.route("/register")
def register():
    login = request.args.get("login")
    password = request.args.get("password")
    password_confirm = request.args.get("password_confirm")

    if not login or not password or not password_confirm:
        return "Please, pass all expected arguments (login, password and password confirmation)"

    if password_confirm != password:
        return "Password and password confirmation do not match"

    if Users.query.where(Users.login == login).all():
        return "The login you passed is already taken"

    db.session.add(Users(login=login, password=password))
    db.session.commit()

    return redirect("/all", code=302)


@app.route("/send")
def send():
    login = request.args.get("login")
    password = request.args.get("password")
    message = request.args.get("message")

    if not login or not password or not message:
        return "Please, pass all expected arguments (login, password, message)"

    response = Users.query.where(Users.login == login).all()
    if response and response[0].password == password:
        db.session.add(Messages(user_id=response[0].id, message=message))
        db.session.commit()
        return redirect("/all", code=302)

    return "Invalid login or password"


@app.route("/all")
def all():
    data = ""

    for message in Messages.query.all():
        user = Users.query.filter(Users.id == message.user_id).all()
        data += (
            f"<b>{user[0].login} [{message.message_date}]:</b> {message.message}<br/>"
        )

    if not data:
        data = "Messages not found"

    return Markup(data)
