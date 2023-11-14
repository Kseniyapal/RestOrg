from rest_framework.test import APIClient
from users.models import User
import pytest

class TestUrlsDrinks():

    @pytest.mark.django_db
    def test_get_menu_drinks_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/drinks/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_menu_drinks_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/drinks/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_menu_item_drink_with_authorized_client(self, get_drinks):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/drinks/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_menu_item_drink_with_guest_client(self, get_drinks):
        guest_client = APIClient()
        response = guest_client.get('/api/drinks/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_item_drink_with_empty_data_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.post('/api/drinks/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_drink_with_empty_data_with_authorized_client_not_super_user(self, get_users):
        authorized_client = APIClient()
        user = get_users[0]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_drink_with_empty_data_with_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_item_drink_with_guest_client(self):
        guest_client = APIClient()
        data = {
        "price": 2
        }
        response = guest_client.patch('/api/drinks/1/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_update_item_drink_with_authorized_not_super_client(self, get_users):
        authorized_client = APIClient()
        data = {
        "price": 2
        }
        user = get_users[0]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.patch('/api/drinks/1/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_update_item_drink_with_authorized_admin(self, get_users):
        authorized_client = APIClient()
        data = {
        "price": 2
        }
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.patch('/api/drinks/1/', data=data, format='json')
        assert response.status_code == 200