"""Configuration loader for SQL Secure Cloud."""
import os
from dotenv import load_dotenv
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-dev-key")
load_dotenv()

# Use Flask's instance folder for database
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
print("📍 Using database at:", db_path)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"

AES_KEY = os.getenv("AES_KEY")
if AES_KEY is not None:
    AES_KEY = AES_KEY.encode()  # Convert to bytes
