from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish, MenuItemDrink
import pytest


class TestUrls():

    @pytest.mark.django_db
    def test_start_page(self):
        guest_client = APIClient()
        response = guest_client.get('/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_list_orders_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_list_orders_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/orders/')
        assert response.status_code == 200

    """@pytest.mark.django_db
    @pytest.mark.parametrize(
    'number, menu_dishes, menu_drinks, waiter',
    [(1, [1, 2], [1, 3], 1)])
    def test_get_order_with_guest_client(self, number, menu_dishes, menu_drinks, waiter):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/1')
        assert response.status_code == 401"""

    @pytest.mark.django_db
    def test_get_menu_dishes_with_guest_client(self):
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

    """@pytest.mark.django_db
    @pytest.mark.parametrize(
    'id, name, image, weight, price',
    [(1, 'Салат', 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg', 100, 5)])
    def test_get_menu_item_dish_with_authorized_client(self, id, name, image, weight, price):
        item = MenuItemDish.objects.get_or_create({
            'id': id,
            'name': name,
            'image' : image,
            'weight' : weight,
            'price' : price,
        })
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/1/')
        assert response.status_code == 200"""
    
    @pytest.mark.django_db
    @pytest.mark.usefixtures("get_dish")
    def test_get_menu_item_dish_with_authorized_client(self, get_dish):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.parametrize(
    'id, name, image, weight, price',
    [(1, 'Салат', 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg', 100, 5)])
    def test_get_menu_item_dish_with_guest_client(self, id, name, image, weight, price):
        item = MenuItemDish.objects.get_or_create({
            'id': id,
            'name': name,
            'image' : image,
            'weight' : weight,
            'price' : price,
        })
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.parametrize(
    'id, name, image, volume, price',
    [(1, 'Салат', 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg', 100, 5)])
    def test_get_menu_item_drink_with_authorized_client(self, id, name, image, volume, price):
        item = MenuItemDrink.objects.get_or_create({
            'id': id,
            'name': name,
            'image' : image,
            'volume' : volume,
            'price' : price,
        })
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/drinks/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.parametrize(
    'id, name, image, volume, price',
    [(1, 'Салат', 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg', 100, 5)])
    def test_get_menu_item_drink_with_guest_client(self, id, name, image, volume, price):
        item = MenuItemDrink.objects.get_or_create({
            'id': id,
            'name': name,
            'image' : image,
            'volume' :volume,
            'price' : price,
        })
        guest_client = APIClient()
        response = guest_client.get('/api/drinks/1/')
        assert response.status_code == 200
    
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

 