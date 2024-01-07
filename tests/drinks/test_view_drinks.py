from orders.models import MenuItemDrink
from rest_framework.test import APIClient
import pytest

class TestViewDrinks():
    @pytest.mark.django_db
    def test_num_list_drink(self, get_drinks):
        guest_client = APIClient()
        response = guest_client.get('/api/drinks/')
        assert len(response.data) == len(get_drinks)

    @pytest.mark.django_db
    def test_data_item_drink(self, get_drinks):
        drink = MenuItemDrink.objects.get_or_create(id=1)
        assert drink[0].name == get_drinks[0].name
        assert drink[0].image == get_drinks[0].image
        assert drink[0].volume == get_drinks[0].volume
        assert drink[0].price == get_drinks[0].price
    
    @pytest.mark.django_db
    def test_data_create_and_get_item_drink_by_admin(self, get_users, get_drinks):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250,
            'price': 12
        }
        authorized_client.post('/api/drinks/', data=data)
        response = authorized_client.get('/api/drinks/3/')
        assert response.data["name"] == data['name']
        assert response.data["image"] == data['image']
        assert response.data["volume"] == data['volume']
        assert response.data["price"] == data['price']

    @pytest.mark.django_db
    def test_data_create_item_drink_by_guest(self, get_users, get_drinks):
        guest_client = APIClient()
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250,
            'price': 12
        }
        response = guest_client.post('/api/drinks/', data=data)
        assert response.data["detail"] == 'Чтобы создать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_data_create_item_drink_by_authorized_client_not_admin(self, get_users, get_drinks):
        authorized_client = APIClient()
        user = get_users[1]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250,
            'price': 12
        }
        response = authorized_client.post('/api/drinks/', data=data)
        assert response.data["detail"] == 'Чтобы создать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_data_create_item_drink_and_get_list_by_admin(self, get_users, get_drinks):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250,
            'price': 12
        }
        authorized_client.post('/api/drinks/', data=data)
        response = authorized_client.get('/api/drinks/')
        assert response.data[2]["name"] == data['name']
        assert response.data[2]["image"] == data['image']
        assert response.data[2]["volume"] == data['volume']
        assert response.data[2]["price"] == data['price']
    
    @pytest.mark.django_db
    def test_data_update_item_drink_with_admin(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        db_data = {
            'name': get_drinks[0].name,
            'image': get_drinks[0].image,
            'volume': get_drinks[0].volume,
        }
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        authenticated_client.patch(f'/api/drinks/{get_drinks[0].id}/', data)
        response = authenticated_client.get(f'/api/drinks/{get_drinks[0].id}/')
        assert response.data['name'] == db_data['name']
        assert response.data['image'] == db_data['image']
        assert response.data['volume'] == db_data['volume']
        assert response.data['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_drink_and_get_list_with_admin(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        db_data = {
            'name': get_drinks[0].name,
            'image': get_drinks[0].image,
            'volume': get_drinks[0].volume,
        }
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        authenticated_client.patch(f'/api/drinks/{get_drinks[0].id}/', data)
        response = authenticated_client.get('/api/drinks/')
        assert response.data[0]['name'] == db_data['name']
        assert response.data[0]['image'] == db_data['image']
        assert response.data[0]['volume'] == db_data['volume']
        assert response.data[0]['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_drink_with_authorized(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/drinks/{get_drinks[0].id}/', data)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."

    @pytest.mark.django_db
    def test_data_update_item_drink_with_guest(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/drinks/{get_drinks[0].id}/', data)
        assert response.data['detail'] == 'Чтобы редактировать пункт меню, вы должны обладать правами администратора.'

    @pytest.mark.django_db
    def test_create_item_drink_without_name_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={
            'image': 'http://127.0.0.1:8000/media/images/Mohito-b-a.jpg',
            'volume': 250,
            'price': 12})
        assert response.data["name"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_drink_without_image_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={'name': 'Мохито',
            'volume': 250,
            'price': 12})
        assert response.data["image"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_drink_without_volume_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={'name': 'Мохито',
            'image': 'http://127.0.0.1:8000/media/images/Mohito-b-a.jpg',
            'price': 12})
        assert response.data["volume"][0] == 'This field is required.'

    @pytest.mark.django_db
    def test_create_item_dish_without_price_by_admin(self, get_users):
        authorized_client = APIClient()
        user = get_users[3]
        authorized_client.force_authenticate(user=user)
        response = authorized_client.post('/api/drinks/', data={'name': 'Салат винегрет',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250})
        assert response.data["price"][0] == 'This field is required.'