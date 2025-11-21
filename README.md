# 🚀 Django Backend Setup (WSL Ubuntu)

This project uses **Django**, **Django REST Framework**, **SimpleJWT**, and **Pytest**.  
Follow the steps below to set up and run the backend on **WSL Ubuntu**.

---

## 🔧 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🐍 2. Install Python & Virtual Environment Tools

WSL Ubuntu typically includes Python 3.x, but install the required tools just in case:

```bash
sudo apt install -y python3 python3-venv python3-pip
```

---

## 🌱 3. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To deactivate:

```bash
deactivate
```

---

## 📦 4. Install Project Dependencies

```bash
pip install     django     djangorestframework     djangorestframework-simplejwt     pytest     pytest-django     PyJWT
```

---

## 🏗️ 5. Initialize the Django Project

```bash
django-admin startproject core .
```

Run the development server to confirm everything is working:

```bash
python manage.py runserver
```

---

## 🧪 6. Run Tests with Pytest

```bash
pytest -v
```

If Pytest doesn’t detect Django settings, ensure `pytest.ini` includes:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = core.settings
```

---

## 🔐 7. JWT Authentication (SimpleJWT)

This project uses **SimpleJWT** for token-based authentication.  
Install optional enhancements with:

```bash
pip install PyJWT
```

---

## 🧹 8. Useful Django Commands

Create a new application:

```bash
python manage.py startapp accounts
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## ✔️ Finished!

Your Django backend is now fully configured on **WSL Ubuntu** with REST, JWT auth, and test support.
