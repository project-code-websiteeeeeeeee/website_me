from flask import Blueprint

view = Blueprint("view","app")

@view.route("/home")
def homes():
    return "test page home"

