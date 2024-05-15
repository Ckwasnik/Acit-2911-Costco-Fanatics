from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from db import db
import datetime


class Program(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    students = relationship('Student', back_populates='program')


class Student(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    program_id = Column(Integer, ForeignKey('program.id'), nullable=False)

    program = relationship('Program', back_populates='students')
    registrations = relationship('Registration', back_populates='student')


class Course(db.Model):
    id = Column(Integer, primary_key=True)
    program_id = Column(Integer, ForeignKey('program.id'), nullable=False)
    name = Column(String(200), nullable=False)
    teacher = Column(String(200), nullable=False)

    registrations = relationship('Registration', back_populates='course')


class Registration(db.Model):
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

    student = relationship('Student', back_populates='registrations')
    course = relationship('Course', back_populates='registrations')



class Program(db.Model):
    # Existing code...

    @staticmethod
    def create(name):
        program = Program(name=name)
        db.session.add(program)
        db.session.commit()
        return program

    def update(self, name):
        self.name = name
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Student(db.Model):
    # Existing code...

    @staticmethod
    def create(name, program_id):
        student = Student(name=name, program_id=program_id)
        db.session.add(student)
        db.session.commit()
        return student

    def update(self, name, program_id):
        self.name = name
        self.program_id = program_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Course(db.Model):
    # Existing code...

    @staticmethod
    def create(program_id, name, teacher):
        course = Course(program_id=program_id, name=name, teacher=teacher)
        db.session.add(course)
        db.session.commit()
        return course

    def update(self, program_id, name, teacher):
        self.program_id = program_id
        self.name = name
        self.teacher = teacher
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
