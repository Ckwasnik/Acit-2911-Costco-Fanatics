from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from models import Course, Registration, Student
from db import db


api_schedule_bp = Blueprint("api_schedule", __name__)

@api_schedule_bp.route("/schedule")
@login_required
def render_schedule():
    student = current_user.student
    if not student:
        return "No student associated with this user.", 404
    registrations = Registration.query.filter_by(student_id=student.id).all()
    course_ids = [registration.course_id for registration in registrations]
    courses = Course.query.filter(Course.id.in_(course_ids)).all()

    return render_template("schedule.html", courses=courses)
