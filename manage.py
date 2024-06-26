from db import db
from app import create_app
from models import Student, Program, Course, Registration, User
import csv
from sqlalchemy.sql import functions as func
from random import randint, random
import random

app = create_app()

def drop_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()

def create_students():
    studentinfo = []
    with open("./data/students.csv", newline='') as csvfile:
        student = csv.DictReader(csvfile, delimiter=',')
        # Iterate over each row in the CSV file
        for row in student:
            name, program = row["name"], row["program"]
            studentinfo.append({"name": name, "program": program})
    with app.app_context():
        db.create_all()
        for info in studentinfo:
            # Create a Student
            student = Student(name=info['name'], program_id=info['program'])
            # Add each student to the database session
            db.session.add(student)
        db.session.commit()

def create_courses():
    courseinfo = []
    with open("./data/courses.csv", newline='') as csvfile:
        course = csv.DictReader(csvfile, delimiter=',')
        # Iterate over each row in the CSV file
        for row in course:
            name, teacher, program_id, credits, dates, cost, start_time, end_time, day, course_duration = row["name"], row["teacher"], row["program_id"], row["credits"], row["dates"], row["cost"], row["start_time"], row["end_time"], row["day"], row['course_duration']
            courseinfo.append({"name": name, "teacher": teacher, "program_id": program_id, "credits": credits, "dates": dates, "cost": cost, "start_time": start_time, "end_time": end_time, "day": day, "course_duration": course_duration})
    with app.app_context():
        db.create_all()
        for info in courseinfo:
            # Create a Course
            course = Course(name=info['name'], teacher=info['teacher'], program_id=info['program_id'], credits=info['credits'], dates=info['dates'], cost=info['cost'], start_time = info['start_time'], end_time =info['end_time'],day=info['day'], course_duration =info['course_duration'])
            # Add each course to the database session
            db.session.add(course)
        # Commit the changes to the database
        db.session.commit()


def create_programs():
    programinfo = []
    with open("./data/programs.csv", newline='') as csvfile:
        program = csv.DictReader(csvfile, delimiter=',')
        # Iterate over each row in the CSV file
        for row in program:
            name = row["name"]
            programinfo.append({"name": name})
    with app.app_context():
        db.create_all()
        for info in programinfo:
            program = Program(name=info['name'])
            db.session.add(program)
        db.session.commit()

def create_registration(amount):
    for _ in range(amount):
        with app.app_context():
            select_student = db.select(Student.id).order_by(func.random()).limit(amount)
            student = db.session.execute(select_student).scalar()

            select_course = db.select(Course.id).order_by(func.random()).limit(amount)
            course = db.session.execute(select_course).scalar()

            registration = Registration(student_id=student, course_id=course)
            db.session.add(registration)

            db.session.commit()

def create_user():
    username = "test"
    password = "test"
    student_id = 5
    admin = User(username=username, password=password, student_id=student_id)
    db.session.add(admin)
    db.session.commit()




if __name__ == "__main__":
    drop_tables()
    create_students()
    create_programs()
    create_courses()
    create_registration(5)

