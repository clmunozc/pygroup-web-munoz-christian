from flask import Blueprint, request, redirect, flash, render_template, url_for
from flask_login import login_user, logout_user
from app.auth.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db

auth = Blueprint("auth",__name__,url_prefix="")

@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember_me = True if request.form.get("remember") else False
        user = User.query.filter_by(email=email).first()
        correct_pass = check_password_hash(user.password, password)
        if not user or not correct_pass:
            flash("e-mail o contraseña incorrecta, intente de nuevo.")
            return redirect(url_for("auth.login"))
        login_user(user, remember=remember_me)

        return redirect(url_for("products.get_products"))

    return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        nm = request.form.get("name")
        user = User.query.filter_by(email=email).first()
        if user:
            message = "Ya existe una cuenta registradea con este e-mail"
            flash(message)
            return redirect(url_for('auth.signup'))
        hash_pass = generate_password_hash(password)
        new_user = User(
            email=email,
            password=hash_pass,
            name=nm)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')
    
