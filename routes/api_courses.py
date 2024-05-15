from flask import Blueprint, jsonify, request, render_template

from db import db
from models import Course

api_courses_bp = Blueprint("api_courses", __name__)

@api_courses_bp.route("/courses")
def course_json():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("courses.html", course=results)

@api_courses_bp.route("/api/courses/<int:course_id>", methods=["DELETE"])
def update_delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully"}), 204