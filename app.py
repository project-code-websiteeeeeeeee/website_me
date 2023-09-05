from flask import Flask
from view import view
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(view)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #3 dấu slashes biểu thị absolute path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) #ko đc trùng
    content = db.Column(db.String(200), nullable=False) #dữ liệu k đc trống
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #show giờ

    def __repr__(self):
        return '<task %r>' %self.id

if __name__=='__main__':    
    app.run(debug=True, port=8000)

