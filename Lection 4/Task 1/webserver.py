import operator
from flask import Flask, render_template, request

app = Flask(__name__)

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate")
def calculate():
    first_value = float(request.args.get("firstValue"))
    second_value = float(request.args.get("secondValue"))
    action = request.args.get("calculateAction")
    return str(f"Your result is {operators[action](first_value, second_value)}")


app.run(host="0.0.0.0", port=8080)
