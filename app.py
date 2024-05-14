from pathlib import Path
from db import db
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for
from models import Program, Student, Course, Registration
from routes.api_courses import api_courses_bp


app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
app.instance_path = Path(".").resolve()

db.init_app(app)

app.register_blueprint(api_courses_bp)


if __name__ == "__main__":
    app.run(debug=True, port=8888)