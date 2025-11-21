import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_profile_requires_jwt():
    user = User.objects.create_user(username="mateus", password="123456")

    client = APIClient()

    # Obter token
    token_response = client.post("/api/auth/token/", {
        "username": "mateus",
        "password": "123456"
    })
    token = token_response.data["access"]

    # Acessar rota protegida
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    profile_response = client.get("/api/profile/")

    assert profile_response.status_code == 200
    assert profile_response.data["username"] == "mateus"
