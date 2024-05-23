import pytest
<<<<<<< HEAD
from unittest.mock import MagicMock
from flask import json
from app import app
from db import db as main_db
=======
import unittest
from app import app, db
>>>>>>> 3214ccb357fb905c31f71d59be5ceab362f3ed38
from models import Course, Student, Registration
from sqlalchemy.orm import Session

<<<<<<< HEAD
@pytest.fixture
def client():
    with app.test_client() as client:
=======
class TestApiCourses(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

        # Create a temporary database for testing
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
        app.config['TESTING'] = True
>>>>>>> 3214ccb357fb905c31f71d59be5ceab362f3ed38
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

<<<<<<< HEAD
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
            response = self.app.delete(f'/api/registration/{registration.id}')
            self.assertEqual(response.status_code, 204)

            # Use Session.get() instead of Query.get()
            with db.session() as session:
                self.assertIsNone(session.get(Registration, registration.id))
>>>>>>> 3214ccb357fb905c31f71d59be5ceab362f3ed38
