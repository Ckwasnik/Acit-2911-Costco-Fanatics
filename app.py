from pathlib import Path
from db import db
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
app.instance_path = Path(".").resolve()

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8888)