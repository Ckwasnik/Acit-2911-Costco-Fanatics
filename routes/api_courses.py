from flask import Blueprint, jsonify, request, render_template, redirect, url_for

from db import db
from models import Course, Student, Registration

api_courses_bp = Blueprint("api_courses", __name__)

@api_courses_bp.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("courses.html", course=results)

@api_courses_bp.route("/api/courses/<int:course_id>/register", methods=["POST"])
def register_course(course_id):
    student_id = 1
    if not student_id:
        return jsonify({"error": "student_id is required"}), 400
    course = Course.query.get_or_404(course_id)
    student = Student.query.get_or_404(student_id)
    registration = Registration(student_id=student_id, course_id=course_id)
    course.is_registered = True
    db.session.add(registration)
    db.session.commit()
    return redirect(url_for('api_courses.course_json'))


@api_courses_bp.route("/api/registration/<int:registration_id>", methods=["DELETE"])
def delete_register(registration_id):
    registration = Registration.query.get_or_404(registration_id)
    course_id = registration.course_id
    course = Course.query.get_or_404(course_id)
    course.is_registered = False
    db.session.delete(registration)
    db.session.commit()
    return redirect(url_for('api_courses.course_json'))

@api_courses_bp.route("/api/courses/<int:course_id>/unregister", methods=["POST"])
def unregister_course(course_id):
    course = Course.query.get_or_404(course_id)
    course.is_registered = False
    db.session.commit()
    return redirect(url_for('api_schedule.render_schedule'))

