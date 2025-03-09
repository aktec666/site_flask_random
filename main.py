from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route("/random")
def random_number():
    return str(random.randint(1, 100))

@app.route("/random2")
def random_number2():
    return render_template("random2.html", number=random.randint(1, 100))


app.run(debug=True)