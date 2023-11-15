from users.models import User
from rest_framework.test import APIClient
import pytest

class TestViewUsers():
    @pytest.mark.django_db
    def test_list_users_with_guest(self, get_users):
        guest_client = APIClient()
        response = guest_client.get('/api/users/')
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    @pytest.mark.django_db
    def test_list_users_with_authorized(self, get_users):
        authenticated_client = APIClient()
        user = User.objects.get(id=2)
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/users/')
        assert len(response.data) == len(get_users)
    
    @pytest.mark.django_db
    def test_get_user_with_guest(self, get_users):
        guest_client = APIClient()
        response = guest_client.get(f'/api/users/{get_users[0].id}/')
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    @pytest.mark.django_db
    def test_get_user_with_authorized(self, get_users):
        authenticated_client = APIClient()
        user = User.objects.get(id=2)
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/users/{get_users[0].id}/')
        assert response.data['detail'] == 'You do not have permission to perform this action.'

    @pytest.mark.django_db
    def test_get_user_with_admin(self, get_users):
        authenticated_client = APIClient()
        user = User.objects.get(id=4)
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/users/{get_users[0].id}/')
        
        assert response.data['id'] == get_users[0].id
        assert response.data['username'] == get_users[0].username
        assert response.data['email'] == get_users[0].email
        assert response.data['role'] == get_users[0].role

    @pytest.mark.django_db
    def test_get_token(self, get_users):
        guest_client = APIClient()
        print(User.objects.all())
        data = {
            "email" : get_users[0].email,
            "password":f"{get_users[0].password}"
        }
        response = guest_client.post('/api/auth/token/login', data=data, format='json')
        print(response.data)
        assert response.data == ''