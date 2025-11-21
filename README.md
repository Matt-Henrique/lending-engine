# 🚀 Django Backend Setup (WSL Ubuntu + Docker)

This project uses **Django**, **Django REST Framework**, **SimpleJWT**, and **Pytest**,
running entirely through **Docker Compose**.

---

## 🐳 1. Install Docker & Docker Compose

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

Restart your WSL terminal after adding yourself to the `docker` group.

---

## ▶️ 2. Start the Application
From the project root (where docker-compose.yml is located):

```bash
docker compose up --build
```

The API will be available at:
```bash
http://localhost:8000/admin/login/
```

---

## 🧪 3. Run Tests Inside the Container

```bash
docker compose exec web pytest -v
```

---

## 👤 4. Create a Superuser (Inside Container)

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🏗️ 5. Useful Django Commands (inside the container)

Apply database migrations:

```bash
docker compose exec web python manage.py migrate
```

Open Django shell:
```bash
docker compose exec web python manage.py shell
```

---

## 🐚 6. Access the Container Shell

```bash
docker compose exec web bash
```

---

## 🧼 7. Stop and Remove Containers

```bash
docker compose down
```

---

## 🔁 8. Rebuild Everything

```bash
docker compose down
docker compose up --build
```

---
