#!/usr/bin/env python3
"""
Defines the User model using SQLAlchemy ORM with secure password hashing via Werkzeug.
"""


from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User model with secure password hashing and session support."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def set_password(self, password: str) -> None:
        """Hashes and stores the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifies a password against the stored hash."""
        return check_password_hash(self.password_hash, password)

class SecureNote(db.Model):
    """Stores AES-encrypted notes linked to a user."""
    __tablename__ = 'secure_notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=False)

    def encrypt_data(self, plaintext, key):
        """Encrypts plaintext using AES (Fernet)."""
        fernet = Fernet(key)
        self.encrypted_data = fernet.encrypt(plaintext.encode())

    def decrypt_data(self, key):
        """Decrypts stored data using AES (Fernet)."""
        fernet = Fernet(key)
        return fernet.decrypt(self.encrypted_data).decode()
