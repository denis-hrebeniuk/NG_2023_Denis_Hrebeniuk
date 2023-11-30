from app import app, db
from app.models import Users, Messages
from flask import request, redirect, render_template
from markupsafe import Markup


def send_html_error(message, redirect_path):
    message += f'<br /><br /><a href="{redirect_path}"><button>Go back</button></a>'
    return Markup(message)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    login = request.form.get("login")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    if not login or not password or not password_confirm:
        return send_html_error(
            "Please, pass all expected arguments (login, password and password confirmation)",
            "register",
        )

    if password_confirm != password:
        return send_html_error(
            "Password and password confirmation do not match", "register"
        )

    if Users.query.where(Users.login == login).all():
        return send_html_error("The login you passed is already taken", "register")

    db.session.add(Users(login=login, password=password))
    db.session.commit()

    return redirect("/all", code=302)


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("send.html")

    login = request.form.get("login")
    password = request.form.get("password")
    message = request.form.get("message")

    if not login or not password or not message:
        return send_html_error(
            "Please, pass all expected arguments (login, password, message)", "send"
        )

    response = Users.query.where(Users.login == login).all()
    if response and response[0].password == password:
        db.session.add(Messages(user_id=response[0].id, message=message))
        db.session.commit()
        return redirect("/all", code=302)

    return send_html_error("Invalid login or password", "send")


@app.route("/all")
def all():
    data = ""

    for message in Messages.query.all():
        user = Users.query.filter(Users.id == message.user_id).all()
        data += (
            f"<b>{user[0].login} [{message.message_date}]:</b> {message.message}<br />"
        )

    if not data:
        data = "Messages not found"

    return render_template("all.html", data=Markup(data))
