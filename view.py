from flask import Blueprint, render_template

view = Blueprint("view","app")

@view.route("/")
def homes():
    return render_template("lol.html",name="gay")



@view.route("/profile/<username>")
def profile(username):
    return render_template("index.html",name=username)