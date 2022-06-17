from flask import Flask, redirect, url_for
from flask import render_template, request, session
from flask import flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "testme"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("name", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def fauxhome():
    return "Hello! Hi there! This is <h1>Flask</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["nm"]
        session["user"] = usr
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = user(user, None)
            db.session.add(usr)
            db.session.commit()

        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            usr = session["user"]
            return render_template("user.html", user=usr)
        return render_template("login.html")

@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        usr = session["user"]
        if request.method== "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = user.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("email was added")
        else:
            if "email" in session:
                email = session["email"]

        #return f"<b>{usr}</b>! You have logged in!"
        return render_template("user.html", email=email, user=usr)
    else:
        flash("You need to login!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        usr = session["user"]
        flash(f"Logout for {usr} was successful.", "info")
    session.pop("user", None)
    session.pop("email",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    "run the code"
    db.create_all()
    app.run(debug = True)