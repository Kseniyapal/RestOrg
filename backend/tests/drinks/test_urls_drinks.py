from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDrink
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
    def test_create_item_drink(self):
        data = {
            'name': 'Мохито',
            'image': 'http://127.0.0.1:8000/media/images/Mohito-b-a.jpg',
            'volume': 250,
            'price': 12
        }
        num = len(MenuItemDrink.objects.all())
        MenuItemDrink.objects.create(**data)
        res_num = len(MenuItemDrink.objects.all())
        assert res_num-num == 1