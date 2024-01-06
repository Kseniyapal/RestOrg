from rest_framework.test import APIClient
from users.models import User
import pytest

class TestUrlsUsers():

    @pytest.mark.dgango_db
    def test_create_token_login(self, get_users):
        guest_client = APIClient()
        data = {
            "email" : get_users[0].email,
            "password": "1234dfghjmk,l"
        }
        response = guest_client.post('/api/auth/token/login/', data=data, format='json')
        assert response.status_code == 200

    @pytest.mark.dgango_db
    def test_create_token_login_with_email(self):
        guest_client = APIClient()
        data = {
            "email" : "frgswe@rwr.ru",
            "password": "1234dfghjmk,l"
        }
        response = guest_client.post('/api/auth/token/login/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.dgango_db
    def test_logout_with_guest(self):
        guest_client = APIClient()
        response = guest_client.get('/api/auth/token/logout/')
        assert response.status_code == 401
    
    @pytest.mark.dgango_db
    def test_logout_with_authorized(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/auth/token/logout/')
        assert response.status_code == 204

    @pytest.mark.django_db
    def test_list_users_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/users/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_users_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/users/')
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_user_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/users/1/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_user_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/users/1/')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_get_user_with_admin_client(self):
        authenticated_client = APIClient()
        user = User.objects.get(id=4)
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/users/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_user_with_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_user_without_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_create_user_guest_client(self):
        guest_client = APIClient()
        response = guest_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_user_with_exist_email_by_admin(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'ivan@ivan.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_with_exist_username_by_admin(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vanya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'ivan@ivan.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_with_wrong_role_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'D',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_without_username_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_without_email_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400
    
    @pytest.mark.django_db
    def test_create_user_without_first_name_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_without_last_name_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'role': 'C',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_without_role_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'email':'v@v.ru',
            'password': 'geuhihfwhfihifuw'
        })
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_user_without_password_by_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.post('/api/users/', data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'v@v.ru'
        })
        assert response.status_code == 400