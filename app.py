import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True
    )