import utils

from decorators import api_wrapper, WebException
from models import db, User

from flask import Blueprint, current_app as app, redirect, request, session

blueprint = Blueprint("user", __name__)

@blueprint.route("/login", methods=["POST"])
@api_wrapper
def user_login():
    form = request.form
    email = form.get("email")
    password = form.get("password")
    logged_in = login_user(email, password)
    if logged_in:
        return {"success": 1, "message": "Success!"}
    raise WebException("Invalid credentials.")

@blueprint.route("/add", methods=["POST"])
@api_wrapper
def user_add():
    form = request.form
    email = form.get("email")
    password = form.get("password")
    confirm_password = form.get("confirm_password")
    admin = form.get("admin")

    if password != confirm_password:
        raise WebException("Passwords do not match.")

    if len(password) < 4:
        raise WebException("Passwords should be at least 4 characters long.")

    user = get_user(email).first()
    if user is not None:
        raise WebException("User with that email already exists.")

    add_user(email, password, admin)
    return {"success": 1, "message": "Success!"}

def login_user(email, password):
    user = get_user(email).first()
    if user is None:
        return False

    if utils.check_password(user.password, password):
        session["email"] = email
        session["admin"] = admin == True
        session["logged_in"] = True
        return True
    return False

def get_user(email=None, uid=None):
    args = {}
    if email:
        args.update({"email": email})
    if uid:
        args.update({"uid": uid})

    user = User.query.filter_by(**args)
    return user

def add_user(email, password, admin):
    user = User(email, password, admin)
    with app.app_context():
        db.session.add(user)
        db.session.commit()

def is_logged_in():
    return "logged_in" in session and session["logged_in"]
