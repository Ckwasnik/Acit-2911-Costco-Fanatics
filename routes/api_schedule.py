from flask import Blueprint, jsonify, request, render_template
from models import Course

from db import db


api_schedule_bp = Blueprint("api_schedule", __name__)

@api_schedule_bp.route("/schedule")
def render_schedule():
    statement = db.select(Course).order_by(Course.name)
    records = db.session.execute(statement)
    results = records.scalars().all()
    return render_template("schedule.html", courses=results)