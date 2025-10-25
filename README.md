# SQL Secure Cloud System (Phase 1 & 2)

A modular Flask-based login system with secure password hashing, session-based access control, encrypted note storage, and polished UX. Built for clarity, reproducibility, and future expansion into encrypted cloud workflows.

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
* `.env` integration for key management
* SecureNote model with encrypted blobs and timestamps
* Flash messages for login, registration, and dashboard feedback
* Note count and last note timestamp on dashboard
* User registration with email uniqueness check
* Clean form styling and error handling
* Pylint/Pylance cleanup for models and routes

---

## 🧱 Folder Structure

```
CodeAlpha_SQL-Secure-Cloud/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── register.html
├── run.py
├── config.py
├── seed_user.py
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

### 4. Seed a Test User

```bash
python seed_user.py
```

### 5. Add `.env` File

```env
AES_KEY=Z3Vuc0FuZEVuY3J5cHRpb25LZXlGb3JDbG91ZFN5c3RlbXM=
```

Use `Fernet.generate_key().decode()` to generate a valid key.

### 6. Run the App

```bash
python run.py
```

Visit: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

---

## 🧪 Test Credentials

| Username | Email                | Password   |
| -------- | -------------------- | ---------- |
| test     | test@securecloud.com | mypassword |

---

## 📦 Phase 3 Roadmap

* 🔐 File encryption for uploads/downloads
* 📜 Audit logging for user actions
* 🧑‍💼 Role-based access control
* 📊 Dashboard analytics
* 🧪 Unit tests and CI integration
* 📦 Dockerized deployment

---

## 👨‍💻 Author

**Muhammad Raza**

---