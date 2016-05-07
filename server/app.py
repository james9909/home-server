from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = open(".secret_key", "rb").read()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
