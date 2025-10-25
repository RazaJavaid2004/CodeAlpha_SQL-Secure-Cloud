#!/usr/bin/env python3
"""App entry point. Starts the SQL Secure Cloud Flask app."""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
