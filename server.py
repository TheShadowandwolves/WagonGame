from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    def __init__(self, username, high_score):
        self.username = username
        self.high_score = high_score
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    high_score = db.relationship('Scores', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.high_score}')"

class Scores(db.Model):
    def __init__(self, score):
        self.score = score
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.score}', '{self.date_posted}')"
