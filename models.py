from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String
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

    registrations = relationship('Registration', back_populates='course', cascade="all, delete-orphan")

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "phone": self.program_id,
            "balance": self.teacher
        }

class Registration(db.Model):
    id = mapped_column(Integer, primary_key=True)
    student_id = mapped_column(ForeignKey(Student.id), nullable=False)
    course_id = mapped_column(ForeignKey(Course.id), nullable=False)

    student = relationship('Student', back_populates='registrations')
    course = relationship('Course', back_populates='registrations')

    def to_json(self):
        return{
            "id": self.id,
            "name": self.student_id,
            "phone": self.course_id,
        }



<<<<<<< HEAD

=======
<<<<<<< HEAD
=======

>>>>>>> developer
>>>>>>> cf
