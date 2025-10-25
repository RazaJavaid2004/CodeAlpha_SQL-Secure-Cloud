# SQL Secure Cloud System (Phase 1–3)

A modular Flask-based login system with secure password hashing, session-based access control, encrypted note and file storage, and polished UX. Built for clarity, reproducibility, and future expansion into encrypted cloud workflows.

---

## 🔐 Features

### ✅ Phase 1: Authentication & Access Control

* Secure user authentication with hashed passwords (Werkzeug)
* Session-based dashboard access
* Modular Flask architecture using Blueprints
* SQLite backend via SQLAlchemy ORM
* Clean HTML templates (`login.html`, `dashboard.html`)
* Pylint-friendly code with docstrings and headers

### ✅ Phase 2: Encrypted Notes & UX Polish

* AES encryption for secure note storage using Fernet keys
* `.env` integration for key management via `python-dotenv`
* SecureNote model with encrypted blobs and timestamps
* Flash messages for login, registration, and dashboard feedback
* Note count and last note timestamp on dashboard
* User registration with email uniqueness check
* Clean form styling and error handling
* Pylint/Pylance cleanup for models and routes

### ✅ Phase 3: File Encryption & Session Security

* Encrypted file uploads using Fernet AES keys
* Secure session management with `.env`-based `SECRET_KEY`
* Consistent database path across all scripts and runtime
* Flash messages for registration success and login errors
* Register link added to login page for seamless onboarding
* Verified dashboard, upload, and note flows with encryption
* Debugger-safe error handling for invalid keys and missing templates

---

## 🧱 Folder Structure

```
CodeAlpha_SQL-Secure-Cloud/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── login.html
│       ├── dashboard.html
│       ├── register.html
│       └── upload.html
├── config.py
├── run.py
├── seed_user.py
├── init_db.py
├── verify_db.py
├── .env
└── venv/
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/RazaJavaid2004/CodeAlpha_SQL-Secure-Cloud.git
cd CodeAlpha_SQL-Secure-Cloud
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # WSL or Git Bash
.\venv\Scripts\Activate.ps1     # PowerShell
```

### 3. Install Dependencies

```bash
pip install flask flask_sqlalchemy werkzeug python-dotenv cryptography
```

### 4. Add `.env` File

```env
SECRET_KEY=your-super-secure-session-key
AES_KEY=Z3Vuc0FuZEVuY3J5cHRpb25LZXlGb3JDbG91ZFN5c3RlbXM=
```

Use `Fernet.generate_key().decode()` to generate a valid AES key.

### 5. Initialize and Seed Database

```bash
python init_db.py
python seed_user.py
python verify_db.py
```

### 6. Run the App

```bash
python run.py
```

Visit: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

---

## 🧪 Test Credentials

| Username | Email                | Password |
| -------- | -------------------- | -------- |
| test     | test@securecloud.com | test123  |

---

## 📦 Phase 4 Roadmap

* 📜 Audit logging for user actions
* 🧑‍💼 Role-based access control
* 📊 Dashboard analytics and activity history
* 🧪 Unit tests and CI integration
* 📦 Dockerized deployment and cloud hosting
* 🔐 Encrypted file downloads and previews

---

## 👨‍💻 Author

**Muhammad Raza**

Backend Engineer | Security Enthusiast | Technical Storyteller

[GitHub](https://github.com/RazaJavaid2004) | [LinkedIn](https://www.linkedin.com/in/muhammadraza2006)

---