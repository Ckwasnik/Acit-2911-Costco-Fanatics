from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from models import Course, Registration, Student
from db import db


api_schedule_bp = Blueprint("api_schedule", __name__)

@api_schedule_bp.route("/schedule")
@login_required
def render_schedule():
    # Get the student associated with the current user
    student = current_user.student

    if not student:
        # Handle case where user has no associated student
        return "No student associated with this user.", 404

    # Query the registrations of the logged-in student
    registrations = Registration.query.filter_by(student_id=student.id).all()

    # Get the course ids from the registrations
    course_ids = [registration.course_id for registration in registrations]

    # Query the courses using the course ids
    courses = Course.query.filter(Course.id.in_(course_ids)).all()

    return render_template("schedule.html", courses=courses)
