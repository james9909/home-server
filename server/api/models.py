import utils

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    aid = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __init__(self, email, password):
        self.email = email
        self.password = utils.hash_password(password)
