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
        #assert len(response.data) == 1
        #assert response.data[0]['id'] == get_dishes[0].id

    @pytest.mark.django_db
    def test_get_menu_dishes_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_authorized_client(self, get_dishes):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/1/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_guest_client(self, get_dishes):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/1/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_item_dish(self):
        data = {
            'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        num = len(MenuItemDish.objects.all())
        MenuItemDish.objects.create(**data)
        res_num = len(MenuItemDish.objects.all())
        assert res_num-num == 1

    @pytest.mark.django_db
    def test_create_item_dish(self):
        data = {
            'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        num = len(MenuItemDish.objects.all())
        MenuItemDish.objects.create(**data)
        res_num = len(MenuItemDish.objects.all())
        assert res_num-num == 1

    """@pytest.mark.django_db
    def test_update_item_dish(self, get_dishes):
        item_dish = get_dishes[0]
        new_price = 1500
    
        with patch('orders.models.MenuItemDish.objects.filter') as mock_get:
            mock_instance = mock_get.return_value
            mock_instance.price = new_price
        
        with patch('orders.models.MenuItemDish.save') as mock_save:
            mock_instance.save()
    
        updated_item_dish = MenuItemDish.objects.get(id=item_dish.id)
        assert updated_item_dish.price == new_price"""
