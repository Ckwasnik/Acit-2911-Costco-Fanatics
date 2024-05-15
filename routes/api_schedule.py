from flask import Blueprint, jsonify, request, render_template

from db import db


api_schedule_bp = Blueprint("api_schedule", __name__)

@api_schedule_bp.route("/schedule")
def render_schedule():
    return render_template("schedule.html")