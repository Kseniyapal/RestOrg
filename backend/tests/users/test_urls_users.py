from rest_framework.test import APIClient
from users.models import User
import pytest

class TestUrlsUsers():
    @pytest.mark.django_db
    def test_list_users_with_guest_client(self, get_users):
        guest_client = APIClient()
        response = guest_client.get('/api/users/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_users_with_authorized_client(self, get_users):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/users/')
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_user_with_guest_client(self, get_users):
        guest_client = APIClient()
        response = guest_client.get('/api/users/1/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_user_with_authorized_client(self, get_users):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/users/1/')
        assert response.status_code == 403

    """@pytest.mark.django_db
    def test_get_user_with_admin_client(self, get_users):
        client = APIClient()
        authenticated_client = APIClient()
        user = User.objects.get(id=2)
        authenticated_client.force_authenticate(user=user)
        response = client.get('/api/users/')
        assert response.status_code == 200"""