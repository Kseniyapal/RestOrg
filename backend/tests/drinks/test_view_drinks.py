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
    def test_num_create_item_drink(self):
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
    
    @pytest.mark.django_db
    def test_data_create_item_dish(self):
        data = {
            'name': 'Сок',
            'image': 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            'volume': 250,
            'price': 12
        }

        MenuItemDrink.objects.create(**data)
        drink =  MenuItemDrink.objects.get_or_create(id=3)
        assert drink[0].name == data['name']
        assert drink[0].image == data['image']
        assert drink[0].volume == data['volume']
        assert drink[0].price == data['price']
    
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
        response= authenticated_client.patch(f'/api/drinks/{get_drinks[0].id}/', data)
        updated_item = MenuItemDrink.objects.get(id=get_drinks[0].id)
        assert response.data['name'] == db_data['name']
        #assert response.data['image'][] == db_data['image']
        assert response.data['volume'] == db_data['volume']
        assert response.data['price'] == data['price']

    @pytest.mark.django_db
    def test_data_update_item_drink_with_authorized(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/dishes/{get_drinks[0].id}/', data)
        updated_item = MenuItemDrink.objects.get(id=get_drinks[0].id)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."

    @pytest.mark.django_db
    def test_data_update_item_drink_with_guest(self, get_users, get_drinks):
        data = {
            'price': 123
        }
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response= authenticated_client.patch(f'/api/dishes/{get_drinks[0].id}/', data)
        updated_item = MenuItemDrink.objects.get(id=get_drinks[0].id)
        assert response.data['detail'] == "Чтобы редактировать пункт меню, вы должны обладать правами администратора."