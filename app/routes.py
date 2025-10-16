#!/usr/bin/env python3
"""
Description: Handles homepage, user login, session management, and dashboard routing.
"""

from flask import Blueprint, render_template, request, redirect, session, url_for
from .models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Redirects homepage to login page."""
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login. Verifies credentials and starts session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        return "Invalid credentials", 401
    return render_template('login.html')

@bp.route('/dashboard')
def dashboard():
    """Displays dashboard for authenticated users."""
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)
