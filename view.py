from flask import Blueprint, render_template

view = Blueprint("view","app")

@view.route("/")
def lol():
    return render_template("index.html",name="gay")

@view.route("/home")
def home():
    return render_template("lol.html")

@view.route("/profile/<username>")
def profile(username):
    return render_template("index.html",name=username)