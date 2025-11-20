# Django Backend Setup (WSL Ubuntu)

This project uses **Django**, **Django REST Framework**, **SimpleJWT**, and **Pytest**.  
Follow the steps below to set up the development environment on **WSL Ubuntu**.

---

## 🚀 1. System Update

```bash
sudo apt update && sudo apt upgrade -y
```

## 🐍 2. Install Python and venv

WSL Ubuntu already includes Python 3.x. Install the required tools:
```bash
sudo apt install -y python3 python3-venv python3-pip
```

## 🌱 3. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To deactivate:
```bash
deactivate
```

## 📦 4. Install Dependencies

```bash
pip install django \
    djangorestframework \
    djangorestframework-simplejwt \
    pytest pytest-django
```

## 🏗️ 5. Start Django Project

```bash
django-admin startproject core .
```

After installation, run the development server:
```bash
python manage.py runserver
```

## 🧪 6. Running Tests

```bash
pytest -v
```

## 🔐 7. Using JWT Authentication

This project uses SimpleJWT.
Install additional optional JWT tools if needed:

```bash
pip install PyJWT
```

## 🧹 8. Common Commands

Create a new app
```bash
python manage.py startapp accounts
```

Apply migrations
```bash
python manage.py migrate
```

Create a superuser
```bash
python manage.py createsuperuser
```
