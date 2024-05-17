from flask import Blueprint, jsonify, request, render_template
from models import Course, Registration, Student

from db import db


api_schedule_bp = Blueprint("api_schedule", __name__)

@api_schedule_bp.route("/schedule")
def render_schedule():
    statement = db.select(Course).order_by(Course.name)
    statement2 = db.select(Registration).order_by(Registration.id)
    records = db.session.execute(statement)
    records2 = db.session.execute(statement2)
    results = records.scalars().all()
    results2 = records2.scalars().all()
    return render_template("schedule.html", courses=results, registrations=results2)
