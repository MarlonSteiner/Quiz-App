import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# use SQLite database
db = SQL("sqlite:///questions.db")

@app.route("/")
def index():

    if not Login:
        render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def index():

    if confirm != password:
        flash("Password does not match");
        password="";

    if register:
        render_template("generator.html");

@app.route("/generator", username=username)
def index():

    if AI:
        # Use API

        render_template("/")

    if SQL:
        # Use Database
        render_template("/")


@app.route("/login", methods=["GET", "POST"])
def index():

    session.clear();

    # Session
    session["username"] = "";
    session["password"] = "";
    return("");
