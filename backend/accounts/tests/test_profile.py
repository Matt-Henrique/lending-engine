import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
def test_profile_via_token_endpoint():
    user = User.objects.create_user(username="mateus", password="123456")

    client = APIClient()

    token_response = client.post("/api/auth/token/", {
        "username": "mateus",
        "password": "123456"
    })
    token = token_response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    profile_response = client.get("/api/profile/")

    assert profile_response.status_code == 200
    assert profile_response.data["username"] == "mateus"

@pytest.mark.django_db
def test_profile_via_refresh_token():
    user = User.objects.create_user(username="mateus", password="123456")
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/api/profile/")

    assert response.status_code == 200
    assert response.data["username"] == "mateus"
