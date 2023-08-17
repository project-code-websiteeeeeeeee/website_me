from flask import Flask
from view import view

app = Flask("app")
app.register_blueprint(view)

# @app.route("/")
# def home():
#     return "that's page home"
# @app.route("/about")
# def about():
#     return "mêmmeme"


app.run(debug=True, port=8000)

