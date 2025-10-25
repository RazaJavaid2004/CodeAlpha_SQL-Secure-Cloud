# pylint: disable=unused-import

"""Initializes the database with all defined tables."""

from app import create_app
from app.models import db, User, SecureNote, EncryptedFile, AuditLog

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully.")
