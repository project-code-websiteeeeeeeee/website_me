from flask import Blueprint, render_template, url_for

view = Blueprint("view","app")

@view.route("/")
def lol():
    return render_template("index.html",name="gay")

@view.route("/home")
def home():
    return render_template("gay.html")

@view.route("/profile/<username>")
def profile(username):
    return render_template("index.html",name=username)