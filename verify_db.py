"""Verifies that all expected tables exist in the database."""

from app import create_app, db

app = create_app()

with app.app_context():
    tables = db.inspect(db.engine).get_table_names()
    print("📦 Tables in database:", tables)
