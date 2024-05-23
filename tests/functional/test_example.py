import pytest
<<<<<<< HEAD
from unittest.mock import MagicMock
from flask import json
from app import app
from db import db as main_db
from models import Course, Student, Registration

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            main_db.create_all()
            yield client

@pytest.fixture
def mocked_db():
    db = MagicMock()
    db.create_all = MagicMock(return_value=None)
    db.session = MagicMock()
    db.session.add = MagicMock()
    db.session.commit = MagicMock()
    db.session.remove = MagicMock()
    db.drop_all = MagicMock()
    return db

def test_course_json(client):
    response = client.get('/courses')
    assert response.status_code == 200
    # Additional assertions can be added based on the expected HTML response
    # e.g., assert b'<title>Courses</title>' in response.data

#def test_register_course(client, mocked_db):
    # Setup initial data
    #mocked_db.session.query(Course).get.return_value = Course(id=1, name="Test Course")
    #mocked_db.session.query(Student).get.return_value = Student(id=1, name="Test Student")
    
    #data = {
        #'student_id': 1
    #}
    #response = client.put('/api/courses/1/register', data=json.dumps(data), content_type='application/json')
    #assert response.status_code == 201
    #assert response.json == {"message": "Registration created successfully"}

def test_register_course_missing_student_id(client):
    data = {}
    response = client.put('/api/courses/1/register', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {"error": "student_id is required"}

def test_register_course_not_found(client):
    data = {
        'student_id': 1
    }
    response = client.put('/api/courses/999/register', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 404

#def test_delete_register(client, mocked_db):
    # Setup initial data
    #mocked_db.session.query(Registration).get.return_value = Registration(id=1, student_id=1, course_id=1)
    
    #response = client.delete('/api/registration/1')
    #assert response.status_code == 204
    #assert response.json == {"message": "Course deleted successfully"}

def test_delete_register_not_found(client):
    response = client.delete('/api/registration/999')
    assert response.status_code == 404

#def test_render_schedule(client):
    #response = client.get('/schedule')
    #assert response.status_code == 200
    # Additional assertions can be added based on the expected HTML response
    # e.g., assert b'<title>Schedule</title>' in response.data
=======
import unittest
from app import app, db
from models import Course, Student, Registration
from sqlalchemy.orm import Session
>>>>>>> 3214ccb357fb905c31f71d59be5ceab362f3ed38

class TestApiCourses(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

<<<<<<< HEAD
"""
Unit Tests
"""

def test_credits():
    test_course = Course("WebDev", "Tim", 4)
    assert test_course.creditLimit(test_course.credits) is True 
=======
        # Create a temporary database for testing
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
            self.populate_db()
>>>>>>> 3214ccb357fb905c31f71d59be5ceab362f3ed38

    def tearDown(self):
        # Clean up the database after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def populate_db(self):
        # Populate the database with some test data
        with app.app_context():
            self.student = Student(name='John Doe', program_id=1)
            self.course = Course(name='Python Programming', teacher='Mr. Smith', program_id=1, credits=3, dates='2024-01-01', cost=100)
            db.session.add_all([self.student, self.course])
            db.session.commit()

    def test_course_json(self):
        # Test the course_json route
        response = self.app.get('/courses')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Python Programming', response.data)

    def test_register_course(self):
        # Test the register_course route
        with app.app_context():
            student = Student.query.first()
            course = Course.query.first()
            data = {'student_id': student.id}
            response = self.app.put(f'/api/courses/{course.id}/register', json=data)
            self.assertEqual(response.status_code, 201)
            registration = Registration.query.filter_by(student_id=student.id, course_id=course.id).first()
            self.assertIsNotNone(registration)

    def test_delete_register(self):
        # Test the delete_register route
        with app.app_context():
            student = Student.query.first()
            course = Course.query.first()
            registration = Registration(student_id=student.id, course_id=course.id)
            db.session.add(registration)
            db.session.commit()

            response = self.app.delete(f'/api/registration/{registration.id}')
            self.assertEqual(response.status_code, 204)

            # Use Session.get() instead of Query.get()
            with db.session() as session:
                self.assertIsNone(session.get(Registration, registration.id))
