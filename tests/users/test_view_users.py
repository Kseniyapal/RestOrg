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
        data = {
            "email" : get_users[0].email,
            "password": "1234dfghjmk,l"
        }
        response = guest_client.post('/api/auth/token/login', data=data)
        assert response.data['auth_token']!= ''

    @pytest.mark.dgango_db
    def test_logout_with_authorized(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        authenticated_client.post('/api/auth/token/logout')
        authenticated_client = APIClient()
        response = authenticated_client.get('/api/orders/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_user_by_admin(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data={
            'id': 3,
            'username': 'Vasya',
            'first_name': 'Vasya',
            'last_name': 'Somov',
            'role': 'C',
            'email':'ivvan@ivan.ru',
            'password': 'geuhihfwhfihifuw'
        }
        authenticated_client.post('/api/users/', data=data)
        response = authenticated_client.get('/api/users/5/')
        assert response.data["email"] == data["email"]
        assert response.data["username"] == data["username"]
        assert response.data["role"] == data["role"]
        assert response.data["first_name"] == data["first_name"]
        assert response.data["last_name"] == data["last_name"]

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
        assert response.data["email"][0] == 'Пользователь with this Электронная почта already exists.'

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
        assert response.data["username"][0] == 'Пользователь with this Имя пользователя already exists.'

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
        assert response.data["role"][0] == '"D" is not a valid choice.'

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
        assert response.data["username"][0] == 'This field is required.'

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
        assert response.data["email"][0] == 'This field is required.'
    
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
        assert response.data["first_name"][0] == 'This field is required.'

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
        assert response.data["last_name"][0] == 'This field is required.'

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
        assert response.data["role"][0] == 'This field is required.'

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
        assert response.data["password"][0] == 'This field is required.'