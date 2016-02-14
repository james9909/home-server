from flask import Flask, redirect, render_template, session

import api

app = Flask(__name__)

app.register_blueprint(api.users.blueprint, url_prefix="/api/users")

with app.app_context():
    from api.models import db, User
    db.init_app(app)
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
