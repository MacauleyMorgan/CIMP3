import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/landing")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True
    )