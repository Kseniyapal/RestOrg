from rest_framework.test import APIClient
from users.models import User
from orders.models import Order, MenuItemDish, MenuItemDrink
import pytest

class TestViewsOrders():

    @pytest.mark.django_db
    def test_get_list_order_with_guest(self, get_orders):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/')
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    @pytest.mark.django_db
    def test_get_list_order_with_admin(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)

    @pytest.mark.django_db
    def test_get_list_order_with_waiter(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)

    @pytest.mark.django_db
    def test_get_list_order_with_bartender(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 5

    @pytest.mark.django_db
    def test_get_list_order_with_cook(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 5

    @pytest.mark.django_db
    def test_get_order_with_cook(self, get_orders, get_users, get_dishes):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "table_number": 1234568,
        "menu_dishes": get_dishes[1].id,
        "status": "NA"
        }
        response = authenticated_client.get(f'/api/orders/{get_orders[1].id}/')
        assert response.data['table_number'] == data['table_number']
        assert response.data['dishes'][0] == data['menu_dishes']
        assert response.data['status'] == data['status']

    @pytest.mark.django_db
    def test_get_order_with_bartender(self, get_orders, get_users, get_drinks):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "table_number": 1234567,
        "menu_drinks": get_drinks[0].id,
        "status": "NA"
        }
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.data['table_number'] == data['table_number']
        assert response.data['drinks'][0] == data['menu_drinks']
        assert response.data['status'] == data['status']

    @pytest.mark.django_db
    def test_get_order_with_admin(self, get_orders, get_users, get_drinks, get_dishes):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "table_number": 1234567,
        "menu_drinks": get_drinks[0].id,
        "menu_dishes":  get_dishes[0].id,
        "status": "NA",
        "comment": ""
        }
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.data['table_number'] == data['table_number']
        assert response.data['drinks'][0] == data['menu_drinks']
        assert response.data['dishes'][0] == data['menu_dishes']
        assert response.data['comment'] == data['comment']
        assert response.data['status'] == data['status']
        
    @pytest.mark.django_db
    def test_get_order_with_waiter(self, get_orders, get_users, get_drinks, get_dishes):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "table_number": 1234567,
        "menu_drinks": get_drinks[0].id,
        "menu_dishes":  get_dishes[0].id,
        "status": "NA",
        "comment": ""
        }
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.data['table_number'] == data['table_number']
        assert response.data['drinks'][0] == data['menu_drinks']
        assert response.data['dishes'][0] == data['menu_dishes']
        assert response.data['comment'] == data['comment']
        assert response.data['status'] == data['status']