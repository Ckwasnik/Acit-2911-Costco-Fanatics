from pathlib import Path
from db import db
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for
from models import Program, Student, Course, Registration


app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
app.instance_path = Path(".").resolve()


db.init_app(app)

@app.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("courses.html", course=results)

@app.route("/students")
def render_student():
    statement = db.select(Student).order_by(Student.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("students.html", student=results)

@app.route("/registration")
def render_registration():
    statement = db.select(Registration).order_by(Registration.id)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("registration.html", registration=results)


if __name__ == "__main__":
    app.run(debug=True, port=8888)