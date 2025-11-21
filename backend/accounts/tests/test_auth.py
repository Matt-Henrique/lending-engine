import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_auth_token_generation():
    User.objects.create_user(username="mateus", password="123456")
    
    client = APIClient()
    response = client.post("/api/auth/token/", {"username":"mateus","password":"123456"}, format="json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    data = {
        "username": "mateus",
        "email": "mateus@example.com",
        "password": "strongpassword123"
    }

    response = client.post("/api/auth/register/", data, format="json")

    assert response.status_code == 201
    assert response.data["username"] == "mateus"
    assert User.objects.filter(username="mateus").exists()
