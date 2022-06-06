from flask import Flask, redirect, url_for
from flask import render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "testme"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/")
def fauxhome():
    return "Hello! Hi there! This is <h1>Flask</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["nm"]
        session["user"] = usr
        return redirect(url_for("user"))
    else:
        if user in session:
            return redirect("user")
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        return f"<b>{usr}</b>! You have logged in!"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)