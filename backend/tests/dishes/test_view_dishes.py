from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish
from unittest.mock import patch
import pytest

class TestViewDishes():
    @pytest.mark.django_db
    def test_num_list_dish(self, get_dishes):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/')
        assert len(response.data) == len(get_dishes)

    @pytest.mark.django_db
    def test_data_item_dish(self, get_dishes):
        dish =  MenuItemDish.objects.get_or_create(id=1)
        assert dish[0].name == get_dishes[0].name
        assert dish[0].image == get_dishes[0].image
        assert dish[0].weight == get_dishes[0].weight
        assert dish[0].price == get_dishes[0].price

    @pytest.mark.django_db
    def test_num_create_item_dish(self):
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
    def test_data_create_item_dish(self):
        data = {
            'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }

        MenuItemDish.objects.create(**data)
        dish =  MenuItemDish.objects.get_or_create(id=3)
        assert dish[0].name == data['name']
        assert dish[0].image == data['image']
        assert dish[0].weight == data['weight']
        assert dish[0].price == data['price']

    @pytest.mark.django_db
    def test_data_update_item_dish_with_admin(self, get_users, get_dishes):
        data = {
            'price': 123
        }
        db_data = {
            'name': get_dishes[0].name,
            'image': get_dishes[0].image,
            'weight': get_dishes[0].weight,
        }
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        updated_item = MenuItemDish.objects.get(id=get_dishes[0].id)
        assert response.data['name'] == db_data['name']
        assert response.data['image'] == db_data['image']
        assert response.data['weight'] == db_data['weight']
        assert response.data['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_dish_with_authorized(self, get_users, get_dishes):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        updated_item = MenuItemDish.objects.get(id=get_dishes[0].id)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."

    @pytest.mark.django_db
    def test_data_update_item_dish_with_guest(self, get_users, get_dishes):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        updated_item = MenuItemDish.objects.get(id=get_dishes[0].id)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."