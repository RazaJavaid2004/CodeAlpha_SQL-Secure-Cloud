#!/usr/bin/env python3
"""
App entry point. Registers blueprint and initializes database.
"""

from flask import Flask
from app.models import db
from app.routes import bp

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
