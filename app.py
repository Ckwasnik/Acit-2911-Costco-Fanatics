from pathlib import Path
from db import db
from flask import Flask
from models import Program, Student, Course, Registration


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
app.instance_path = Path(".").resolve()

db.init_app(app)

@app.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    course = records.scalars().all()
    return render_template("customers.html", course=course)

@app.route("/students")
def student_json():
    with app_context():
        students = Student.query.order_by(Student.name).all()
    return render_template("students.html", student=student)

@app.route("/programs")
def program_json():
    with app_context():
        programs = Program.query.order_by(Program.name).all()
    return render_template("programs.html", program=program)



if __name__ == "__main__":
    app.run(debug=True, port=8888)