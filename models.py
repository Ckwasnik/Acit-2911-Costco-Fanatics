from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, Time
from sqlalchemy.orm import mapped_column, relationship
from db import db
import datetime
from pathlib import Path
from db import db
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

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
    user = db.relationship('User', back_populates='student', uselist=False)


class Course(db.Model):
    id = mapped_column(Integer, primary_key=True)
    program_id = mapped_column(ForeignKey(Program.id), nullable=False)
    name = mapped_column(String(200), nullable=False)
    teacher = mapped_column(String(200), nullable=False)
    credits = mapped_column(Integer, nullable=False)
    dates = mapped_column(String(200), nullable=False)
    cost = mapped_column(Integer, nullable=False)
    start_time = mapped_column(Integer)
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
    
class User(db.Model, UserMixin):
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(20), nullable=False, unique=True)
    password = mapped_column(String(80), nullable=False)
    student_id = mapped_column(Integer, ForeignKey('student.id'))

    student = relationship('Student', back_populates='user')


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'This username has already been taken. Please choose a different one.')
    
    def validate_student_id(self, student_id):
        student = Student.query.get(student_id.data)
        if not student:
            raise ValidationError('No student found with this ID.')
        existing_user_student = User.query.filter_by(student_id=student_id.data).first()
        if existing_user_student:
            raise ValidationError('A user account for this student ID already exists.')

        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


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
