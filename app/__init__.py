"""App factory and database initialization for SQL Secure Cloud."""

from flask import Flask
from .models import db
from .routes import bp

def create_app():
    """Creates and configures the Flask application."""

    app = Flask(__name__)
    app.config.from_object('config')
    app.secret_key = app.config['SECRET_KEY']

    db.init_app(app)
    app.register_blueprint(bp)

    return app
