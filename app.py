import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",   methods =['GET', 'POST'])
def landing():
    if request.method == 'POST':
        email = request.form.get("sign-in-email-address")
        password = request.form.get("password")
        user = [email, password]
        print(user)
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


@app.route("/register", methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = [first_name, last_name, email, password]
        print(user)
    return render_template("register.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True
    )