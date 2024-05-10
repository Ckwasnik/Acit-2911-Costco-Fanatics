from flask import Blueprint, render_template, redirect, url_for
from models import Program, Student, Course, Registration
from db import db

html_bp = Blueprint("html", __name__)


@html_bp.route("/")
def homepage():
    return render_template("home.html")

@html_bp.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("courses.html", course=results)

@html_bp.route("/students")
def student_json():
    statement = db.select(Student).order_by(Student.name)
    records = db.session.execute(statement)
    student = records.scalars().all()
    return render_template("students.html", student=student)

@html_bp.route("/programs")
def program_json():
    statement = db.select(Program).order_by(Program.name)
    records = db.session.execute(statement)
    program = records.scalars().all()
    return render_template("programs.html", program=program)

@html_bp.route("/registration")
def registration_json():
    statement = db.select(Registration).order_by(Registration.name)
    records = db.session.execute(statement)
    register = records.scalars().all()
    return render_template("registration.html", register=register)