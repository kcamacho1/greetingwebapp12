from flask import Flask, request, render_template
# from flask.templating import render_template
import flask
from flask.helpers import flash

app = Flask(__name__)
app.secret_key = "mannagethem4565"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")  
    return render_template("index.html")
    