"""Seeds the database with a default test user for login verification."""

from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    user = User(username='test', email='test@example.com')
    user.set_password('test123')
    db.session.add(user)
    db.session.commit()
    print("✅ Test user created.")
