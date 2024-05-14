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