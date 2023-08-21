from flask import Flask
from view import view
from flask_sqlalchemy import SQLAlchemy

import sys
print(sys.executable)

app = Flask(__name__)
app.register_blueprint(view)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #3 dấu slashes biểu thị absolute path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)


if __name__=='__main__':    
    app.run(debug=True, port=8000)

