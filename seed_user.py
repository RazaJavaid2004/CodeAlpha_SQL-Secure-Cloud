"""
Creates a test user for SQL Secure Cloud System Phase 1.
"""

from app import models
from run import app

with app.app_context():
    models.db.create_all()  # Creates tables if not already created

    user = models.User(username='test', email='test@securecloud.com')
    user.set_password('mypassword')

    models.db.session.add(user)
    models.db.session.commit()

    print("✅ User 'test' created successfully.")
