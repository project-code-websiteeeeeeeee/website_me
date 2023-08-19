from flask import Flask
from view import view

app = Flask("app")
app.register_blueprint(view)



app.run(debug=True, port=8000)

