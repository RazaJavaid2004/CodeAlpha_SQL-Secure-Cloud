from run import app
from app import models

with app.app_context():
    models.db.create_all()
