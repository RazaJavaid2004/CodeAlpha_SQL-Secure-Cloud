"""
Handles homepage, user login, session management, secure note encryption, and dashboard rendering.
"""

import os
import io

from flask import send_file
from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from dotenv import load_dotenv
from cryptography.fernet import Fernet

from .models import User, SecureNote, EncryptedFile, AuditLog, db

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

            # ✅ Log the login
            log = AuditLog(user_id=user.id, action="Logged in")
            db.session.add(log)
            db.session.commit()

            flash("Login successful!", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password.", "danger")

    return render_template('login.html')

@bp.route('/logout')
def logout():
    """Logs out the current user and clears the session."""
    user_id = session.get('user_id')

    if user_id:
        # ✅ Log the logout
        log = AuditLog(user_id=user_id, action="Logged out")
        db.session.add(log)
        db.session.commit()

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
    """Displays decrypted notes and uploaded files for the logged-in user."""
    if 'user_id' not in session:
        flash("Please log in to view your dashboard.", "warning")
        return redirect(url_for('main.login'))

    user = User.query.get(session['user_id'])
    if user is None:
        flash("User not found. Please log in again.", "danger")
        return redirect(url_for('main.login'))

    # Decrypted notes
    notes = SecureNote.query.filter_by(user_id=user.id).all()
    decrypted_notes = [note.decrypt_data(AES_KEY) for note in notes]
    note_count = len(decrypted_notes)

    # Uploaded encrypted files
    uploaded_files = EncryptedFile.query.filter_by(user_id=user.id).all()

    return render_template(
        'dashboard.html',
        user=user,
        notes=decrypted_notes,
        note_count=note_count,
        files=uploaded_files
    )

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    """Handles encrypted file upload and storage."""
    if 'user_id' not in session:
        flash("Login required to upload files.", "warning")
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        uploaded_file = request.files['file']
        if not uploaded_file:
            flash("No file selected.", "danger")
            return redirect(url_for('main.upload'))

        raw_data = uploaded_file.read()
        filename = uploaded_file.filename or "unnamed_file"

        if AES_KEY is None:
            flash("Encryption key missing or invalid.", "danger")
            return redirect(url_for('main.dashboard'))

        encrypted_blob = Fernet(AES_KEY).encrypt(raw_data)

        encrypted_file = EncryptedFile(
            user_id=session['user_id'],
            filename=filename,
            encrypted_data=encrypted_blob
        )
        db.session.add(encrypted_file)

        # ✅ Log the upload in AuditLog
        log = AuditLog(
            user_id=session['user_id'],
            action=f"Uploaded encrypted file: {filename}"
        )
        db.session.add(log)

        db.session.commit()

        flash(f"File '{filename}' uploaded and encrypted successfully!", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('upload.html')

@bp.route('/download/<int:file_id>')
def download(file_id):
    """Decrypts and sends the requested file to the user."""
    if 'user_id' not in session:
        flash("Login required to download files.", "warning")
        return redirect(url_for('main.login'))

    file = EncryptedFile.query.get_or_404(file_id)

    if file.user_id != session['user_id']:
        flash("Unauthorized access to file.", "danger")
        return redirect(url_for('main.dashboard'))

    if AES_KEY is None:
        flash("Encryption key is missing. Please check your .env setup.", "danger")
        return redirect(url_for('main.dashboard'))

    decrypted_data = Fernet(AES_KEY).decrypt(file.encrypted_data)

    # ✅ Log the download in AuditLog
    log = AuditLog(
        user_id=session['user_id'],
        action=f"Downloaded encrypted file: {file.filename}"
    )
    db.session.add(log)
    db.session.commit()

    return send_file(
        io.BytesIO(decrypted_data),
        download_name=file.filename,
        as_attachment=True
    )
