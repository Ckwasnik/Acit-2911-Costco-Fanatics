from pathlib import Path
from db import db
from flask import Flask, render_template, jsonify, request, redirect, url_for
from models import Program, Student, Course, Registration
from routes.html_bp import html_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
app.instance_path = Path(".").resolve()

db.init_app(app)

# Route to retrieve course data
@app.route("/courses")
def get_courses():
    courses = Course.query.order_by(Course.name).all()
    return render_template("courses.html", courses=courses)

# Route to retrieve student data
@app.route("/students")
def get_students():
    students = Student.query.order_by(Student.name).all()
    return render_template("students.html", students=students)

# Route to retrieve program data
@app.route("/programs")
def get_programs():
    programs = Program.query.order_by(Program.name).all()
    return render_template("programs.html", programs=programs)

# Route to add a new course
@app.route("/courses/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        # Create a new Course object
        new_course = Course(name=name, description=description)
        # Add the new course to the database
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for("get_courses"))
    return render_template("add_course.html")

# Route to edit an existing course
@app.route("/courses/edit/<int:course_id>", methods=["GET", "POST"])
def edit_course(course_id):
    course = Course.query.get(course_id)
    if request.method == "POST":
        course.name = request.form["name"]
        course.description = request.form["description"]
        db.session.commit()
        return redirect(url_for("get_courses"))
    return render_template("edit_course.html", course=course)

# Route to delete an existing course
@app.route("/courses/delete/<int:course_id>", methods=["POST"])
def delete_course(course_id):
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for("get_courses"))

# Route to retrieve all courses
@app.route("/courses")
def get_courses():
    courses = Course.query.all()
    return render_template("courses.html", courses=courses)

if __name__ == "__main__":
    app.run(debug=True, port=8888)