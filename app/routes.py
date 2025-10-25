"""
Handles homepage, user login, session management, secure note encryption, and dashboard rendering.
"""

import os

from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from dotenv import load_dotenv
from cryptography.fernet import Fernet

from .models import User, SecureNote, db

load_dotenv()

# Load and validate AES key from .env
raw_key = os.getenv('AES_KEY')
AES_KEY = None
if raw_key:
    try:
        AES_KEY = raw_key.encode()
        Fernet(AES_KEY)  # Validate key format
    except ValueError:
        print("❌ Invalid AES_KEY in .env — must be 32 url-safe base64-encoded bytes.")

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    """Redirects to login or dashboard based on session."""
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handles new user registration and account creation."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash("Username already taken. Please choose another.", "warning")
            return redirect(url_for('main.register'))

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Try logging in or use a different email.", "warning")
            return redirect(url_for('main.register'))

        # Create and save new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('main.login'))

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login and session setup."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            flash("Login successful!", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password.", "danger")

    return render_template('login.html')

@bp.route('/logout')
def logout():
    """Logs out the current user and clears the session."""
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.login'))

@bp.route('/add_note', methods=['POST'])
def add_note():
    """Encrypts and stores a secure note for the logged-in user."""
    if 'user_id' not in session:
        flash("Login required to add notes.", "warning")
        return redirect(url_for('main.login'))

    if AES_KEY is None:
        flash("Encryption key missing or invalid.", "danger")
        return redirect(url_for('main.dashboard'))

    note = request.form['note']
    secure_note = SecureNote()
    secure_note.user_id = session['user_id']
    secure_note.encrypt_data(note, AES_KEY)
    db.session.add(secure_note)
    db.session.commit()

    flash("Secure note saved successfully!", "success")
    return redirect(url_for('main.dashboard'))

@bp.route('/dashboard')
def dashboard():
    """Displays decrypted notes for the logged-in user."""
    if 'user_id' not in session:
        flash("Please log in to view your dashboard.", "warning")
        return redirect(url_for('main.login'))

    user = User.query.get(session['user_id'])
    if user is None:
        flash("User not found. Please log in again.", "danger")
        return redirect(url_for('main.login'))

    notes = SecureNote.query.filter_by(user_id=user.id).all()
    decrypted_notes = [note.decrypt_data(AES_KEY) for note in notes]
    note_count = len(decrypted_notes)

    return render_template('dashboard.html', user=user, notes=decrypted_notes,
                           note_count=note_count)
