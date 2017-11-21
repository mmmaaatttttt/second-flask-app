from flask import Flask, render_template, request
from random import random

app = Flask(__name__)

@app.route("/introduce")
def introduce():
    return render_template("introduce.html")

@app.route("/greet")
def greet():
    first_name = request.args['first_name'].title()
    last_name = request.args['last_name'].title()
    return render_template(
        "greet.html",
        first_name=first_name,
        last_name=last_name
    )

@app.route("/")
def say_hi():
    return render_template("index.html")

@app.route("/bye")
def say_bye():
    return render_template("bye.html")

@app.route("/sweet")
def sweet():
    return render_template("sweet.html")

@app.route("/fruits")
def fruits():
    fruits = ["apples", "bananas", "cherries", "durians"]
    return render_template("fruits.html", fruits=fruits)

@app.route("/feeling_lucky")
def coin_flip():
    fruit = "apple"
    return render_template(
        "random.html",
        matt=random(),
        fruit=fruit
    )

if __name__ == "__main__": 
    app.run(debug=True)










