from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

"""@app.route("/")
def fauxhome():
    return "Hello! Hi there! This is <h1>Flask</h1>"

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name)
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"Hi <b>{usr}</b>! You have logged in!"

if __name__ == "__main__":
    app.run(debug = True)