from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish
from unittest.mock import patch
import pytest

class TestUrlsDishes():

    @pytest.mark.django_db
    def test_get_menu_dishes_with_guest_client(self, get_dishes):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_menu_dishes_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/1/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/1/')
        assert response.status_code == 200


    @pytest.mark.django_db
    def test_create_item_dish_with_empty_data_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.post('/api/dishes/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_dish_with_empty_data_with_authorized_client_not_super_user(self, get_users):
        authorized_client = APIClient()
        user = get_users[0]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_dish_with_empty_data_with_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_item_dish_with_guest_client(self):
        guest_client = APIClient()
        data = {
        "price": 2
        }
        response = guest_client.patch('/api/dishes/1/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_update_item_dish_with_authorized_not_super_client(self, get_users):
        authorized_client = APIClient()
        data = {
        "price": 2
        }
        user = get_users[0]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.patch('/api/dishes/1/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_update_item_dish_with_authorized_admin(self, get_users):
        authorized_client = APIClient()
        data = {
        "price": 2
        }
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.patch('/api/dishes/1/', data=data, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_item_dish(self):
        guest_client = APIClient()
        response = guest_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12})
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_create_item_dish_by_authorized_client_not_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[2]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12})
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_create_item_dish_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12})
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_item_dish_without_name_by_authorized_client(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_dish_without_image_by_authorized_client(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'weight': 250,
            'price': 12})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_dish_without_weight_by_authorized_client(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'price': 12})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_item_dish_without_price_by_authorized_client(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250})
        assert response.status_code == 400