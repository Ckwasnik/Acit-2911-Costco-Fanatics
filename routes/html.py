from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from models import Course, Registration, Student, User, LoginForm, RegisterForm
from db import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from extensions import bcrypt

html_bp = Blueprint("html", __name__)


@html_bp.route("/", methods=["GET", "POST"])
def render_homepage():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('api_courses.course_json'))
    return render_template('login.html', form=form)


@html_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        student = Student(name=form.username.data, program_id= 1)
        db.session.add(student)
        new_user = User(username=form.username.data, password=hashed_password, student_id=student.id)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('html.render_homepage'))

    return render_template('register.html', form=form)