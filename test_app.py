import unittest
from app import app, db
from models import Course, Student, Registration

class TestApiCourses(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

        # Create a temporary database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
            self.populate_db()

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
            self.assertIsNone(Registration.query.get(registration.id))

    def test_add_student(self):
        # Test the add student route
        data = {'name': 'Jane Doe', 'program_id': 1}
        response = self.app.post('/api/students', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Jane Doe', response.data)

    def test_delete_student(self):
        # Test the delete student route
        with app.app_context():
            student = Student.query.first()
            response = self.app.delete(f'/api/students/{student.id}')
            self.assertEqual(response.status_code, 204)
            self.assertIsNone(Student.query.get(student.id))

if __name__ == '__main__':
    unittest.main()
