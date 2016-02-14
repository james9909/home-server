import utils

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    uid = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    admin = db.Column(db.Boolean)

    def __init__(self, email, password, admin):
        self.email = email
        self.password = utils.hash_password(password)
        self.admin = admin
