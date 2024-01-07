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
        drink = MenuItemDish.objects.get_or_create(id=1)
        assert drink[0].name == get_dishes[0].name
        assert drink[0].image == get_dishes[0].image
        assert drink[0].weight == get_dishes[0].weight
        assert drink[0].price == get_dishes[0].price
    
    @pytest.mark.django_db
    def test_data_create_and_get_item_dish_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        authorized_client.post('/api/dishes/', data=data)
        response = authorized_client.get('/api/dishes/3/')
        assert response.data["name"] == data['name']
        assert response.data["image"] == data['image']
        assert response.data["weight"] == data['weight']
        assert response.data["price"] == data['price']

    @pytest.mark.django_db
    def test_data_create_item_dish_by_guest(self, get_users):
        guest_client = APIClient()
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        response = guest_client.post('/api/dishes/', data=data)
        assert response.data["detail"] == 'Чтобы создать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_data_create_item_dish_by_authorized_client_not_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[1]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        response = authorized_client.post('/api/dishes/', data=data)
        assert response.data["detail"] == 'Чтобы создать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_data_create_item_dish_and_get_list_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'weight': 250,
            'price': 12
        }
        authorized_client.post('/api/dishes/', data=data)
        response = authorized_client.get('/api/dishes/')
        assert response.data[2]["name"] == data['name']
        assert response.data[2]["image"] == data['image']
        assert response.data[2]["weight"] == data['weight']
        assert response.data[2]["price"] == data['price']
    
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
        authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        response = authenticated_client.get(f'/api/dishes/{get_dishes[0].id}/')
        assert response.data['name'] == db_data['name']
        assert response.data['image'] == db_data['image']
        assert response.data['weight'] == db_data['weight']
        assert response.data['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_dish_and_get_list_with_admin(self, get_users, get_dishes):
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
        authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        response = authenticated_client.get('/api/dishes/')
        assert response.data[0]['name'] == db_data['name']
        assert response.data[0]['image'] == db_data['image']
        assert response.data[0]['weight'] == db_data['weight']
        assert response.data[0]['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_dish_with_authorized(self, get_users, get_dishes):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."

    @pytest.mark.django_db
    def test_data_update_item_dish_with_guest(self, get_users, get_dishes):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.patch(f'/api/dishes/{get_dishes[0].id}/', data)
        assert response.data['detail'] == 'Чтобы редактировать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_create_item_dish_without_name_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={
            'image': 'http://127.0.0.1:8000/media/images/Mohito-b-a.jpg',
            'weight': 250,
            'price': 12})
        assert response.data["name"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_dish_without_image_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Мохито',
            'weight': 250,
            'price': 12})
        assert response.data["image"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_dish_without_weight_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Мохито',
            'image': 'http://127.0.0.1:8000/media/images/Mohito-b-a.jpg',
            'price': 12})
        assert response.data["weight"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_dish_without_price_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/dishes/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250})
        assert response.data["price"][0] == 'This field is required.'