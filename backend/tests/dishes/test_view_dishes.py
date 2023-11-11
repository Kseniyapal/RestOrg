from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish
from unittest.mock import patch
import pytest

class TestViewDishes():
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