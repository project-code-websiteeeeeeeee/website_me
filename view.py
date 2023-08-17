from flask import Blueprint, render_template

view = Blueprint("view","app")

@view.route("/home")
def homes():
    return render_template("index.html",name="gay")

@view.route("/")