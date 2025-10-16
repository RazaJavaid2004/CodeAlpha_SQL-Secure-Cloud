# SQL Secure Cloud System (Phase 1)

A modular Flask-based login system with secure password hashing, session-based access control, and clean dashboard rendering. Built for clarity, reproducibility, and future expansion into encrypted cloud workflows.

---

## 🔐 Features

- Secure user authentication with hashed passwords (Werkzeug)
- Session-based dashboard access
- Modular Flask architecture using Blueprints
- SQLite backend via SQLAlchemy ORM
- Clean HTML templates (`login.html`, `dashboard.html`)
- Pylint-friendly code with docstrings and headers

---

## 🧱 Folder Structure

```

CodeAlpha_SQL-Secure-Cloud/
├── app/
│   ├──  **init** .py
│   ├── models.py
│   └── routes.py
├── templates/
│   ├── login.html
│   └── dashboard.html
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
pip install flask flask_sqlalchemy werkzeug
```

### 4. Seed a Test User

```bash
python seed_user.py
```

### 5. Run the App

```bash
python run.py
```

Visit: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

---

## 🧪 Test Credentials

| Username | Email                | Password   |
| -------- | -------------------- | ---------- |
| test    | test@securecloud.com | mypassword |

---

## 📦 Phase 2 Roadmap

* 🔓 Registration and logout routes
* 🔐 AES-encrypted fields for sensitive data
* 🧾 Modular dashboard with user roles
* 🧪 Unit tests and CI integration
* 📦 Dockerized deployment

---

## 👨‍💻 Author

**Muhammad Raza**

---