from flask import Flask
from app.routes import students_bp


def create_app():
    """Application factory: builds and configures the Flask app."""
    app = Flask(__name__)
    app.register_blueprint(students_bp)
    return app
