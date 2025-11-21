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
