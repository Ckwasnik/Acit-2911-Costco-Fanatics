from flask import Blueprint, jsonify, request, render_template

from db import db
from models import Course, Student, Registration

api_courses_bp = Blueprint("api_courses", __name__)

@api_courses_bp.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("courses.html", course=results)

@api_courses_bp.route("/api/courses/<int:course_id>/register", methods=["PUT"])
def register_course(course_id):
    data = request.json
    student_id = data.get('student_id')
    if student_id is None:
        return jsonify({"error": "student_id is required"}), 400
    
    course = db.session.get(Course, course_id)
    if course is None:
        return jsonify({"error": "Course not found"}), 404
    
    student = db.session.get(Student, student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    
    registration = Registration(student_id=student_id, course_id=course_id)
    db.session.add(registration)
    db.session.commit()
    return jsonify({"message": "Registration created successfully"}), 201

@api_courses_bp.route("/api/registration/<int:registration_id>", methods=["DELETE"])
def delete_register(registration_id):
    registration = db.session.get(Registration, registration_id)
    if registration is None:
        return jsonify({"error": "Registration not found"}), 404
    
    db.session.delete(registration)
    db.session.commit()
    return jsonify({"message": "Registration deleted successfully"}), 204
