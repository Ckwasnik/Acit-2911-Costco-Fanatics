from pathlib import Path
from flask import Flask
from extensions import db, bcrypt, login_manager
from models import User
from routes.api_courses import api_courses_bp
from routes.api_schedule import api_schedule_bp
from routes.html import html_bp

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqdatabase.db"
    app.instance_path = Path(".").resolve()
    app.config['SECRET_KEY'] = 'thisisasecretkey'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(api_courses_bp)
    app.register_blueprint(api_schedule_bp)
    app.register_blueprint(html_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=4000)
