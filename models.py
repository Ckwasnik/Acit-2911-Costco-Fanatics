from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, Time
from sqlalchemy.orm import mapped_column, relationship
from db import db
import datetime

class Program(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False)

    students = relationship('Student', back_populates='program')


class Student(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False)
    program_id = mapped_column(ForeignKey(Program.id), nullable=False)

    program = relationship('Program', back_populates='students')
    registrations = relationship('Registration', back_populates='student')


class Course(db.Model):
    id = mapped_column(Integer, primary_key=True)
    program_id = mapped_column(ForeignKey(Program.id), nullable=False)
    name = mapped_column(String(200), nullable=False)
    teacher = mapped_column(String(200), nullable=False)
    credits = mapped_column(Integer, nullable=False)
    dates = mapped_column(String(200), nullable=False)
    cost = mapped_column(Integer, nullable=False)
    start_time = mapped_column(Integer, nullable=False)
    end_time = mapped_column(Integer, nullable=False)
    course_duration = mapped_column(Integer, nullable=False)
    day = mapped_column(String, nullable=False)
    is_registered = mapped_column(Boolean, default=False) 

    registrations = relationship('Registration', back_populates='course', cascade="all, delete-orphan")

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "program_id": self.program_id,
            "teacher": self.teacher
        }

    def __init__(self, name, teacher, credits):
        if type(name) and type(teacher) is not str:
            raise AttributeError
        if type(credits) is not int:
            raise AttributeError

        self.name = name
        self.teacher = teacher
        self.credits = credits


    def creditLimit(self, credits):
        if self.credits > 4:
            return False
        else:
            return True
            
    

class Registration(db.Model):
    id = mapped_column(Integer, primary_key=True)
    student_id = mapped_column(ForeignKey(Student.id), nullable=False)
    course_id = mapped_column(ForeignKey(Course.id), nullable=False)

    student = relationship('Student', back_populates='registrations')
    course = relationship('Course', back_populates='registrations')

    def to_json(self):
        return{
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
        }

    def __init__(self, student_id, course_id):
        if type(student_id) is not int:
            raise AttributeError 
        if type(course_id) is not int:
            raise AttributeError        
        self.student_id = student_id
        self.course_id = course_id





<<<<<<< HEAD

=======
<<<<<<< HEAD
=======

>>>>>>> developer
>>>>>>> cf
