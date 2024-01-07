from django.shortcuts import get_object_or_404
from rest_framework.test import APIClient
from users.models import User
from orders.models import Order, MenuItemDish, MenuItemDrink
import pytest

class TestViewsOrders():

    @pytest.mark.django_db
    def test_views_get_list_order_with_guest(self, get_orders):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/')
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    @pytest.mark.django_db
    def test_views_get_list_order_with_admin(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)

    @pytest.mark.django_db
    def test_views_get_list_order_with_waiter(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)

    @pytest.mark.django_db
    def test_views_get_list_order_with_bartender(self, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 7

    @pytest.mark.django_db
    def test_views_get_list_order_with_cook(self, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 7

    @pytest.mark.django_db
    def test_views_get_order_with_cook(self, get_orders, get_users, get_dishes):
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
    def test_views_get_order_with_bartender(self, get_orders, get_users, get_drinks):
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
    def test_views_get_order_with_admin(self, get_orders, get_users, get_drinks, get_dishes):
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
    def test_views_get_order_with_waiter(self, get_orders, get_users, get_drinks, get_dishes):
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


    @pytest.mark.django_db
    def test_views_create_order_with_guest_client(self, get_users):
        guest_client = APIClient()
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        guest_client.post('/api/orders/', data=data, format='json')
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get('/api/orders/10/')
        assert response.data["table_number"] == data["number"]
        assert response.data["dishes"] == data["menu_dishes"]
        assert response.data["drinks"] == data["menu_drinks"]
        assert response.data["waiter"] == data["waiter"]

    @pytest.mark.django_db
    def test_views_create_order_with_waiter_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": None
        }
        authenticated_client.post('/api/orders/', data=data, format='json')
        response = authenticated_client.get('/api/orders/10/')
        assert response.data["table_number"] == data["number"]
        assert response.data["dishes"] == data["menu_dishes"]
        assert response.data["drinks"] == data["menu_drinks"]
        assert response.data["waiter"] == data["waiter"]

    @pytest.mark.django_db
    def test_views_create_order_with_bartender_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        response = authenticated_client.get('/api/orders/10/')
        assert response.data["table_number"] == data["number"]
        assert response.data["drinks"] == data["menu_drinks"]

    @pytest.mark.django_db
    def test_views_create_order_with_cook_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        response = authenticated_client.get('/api/orders/10/')
        assert response.data["table_number"] == data["number"]
        assert response.data["dishes"] == data["menu_dishes"]

    @pytest.mark.django_db
    def test_views_create_order_with_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        response = authenticated_client.get('/api/orders/10/')
        assert response.data["table_number"] == data["number"]
        assert response.data["dishes"] == data["menu_dishes"]
        assert response.data["drinks"] == data["menu_drinks"]
        assert response.data["waiter"] == data["waiter"]

    @pytest.mark.django_db
    def test_views_create_order_with_no_waiter(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 1
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        assert response.data[0] == 'Надо указать официанта исполнителем'

    @pytest.mark.django_db
    def test_views_create_order_without_dishes_drinks_(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        assert response.data['menu_dishes'][0] == 'This field is required.'
        assert response.data['menu_drinks'][0] == 'This field is required.'
    
    @pytest.mark.django_db
    def test_views_update_order_with_waiter_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data['waiter'] == data['waiter']

    @pytest.mark.django_db
    def test_views_update_order_with_no_waiter_data(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 3
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data[0] == 'Надо указать официанта исполнителем'

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_NA_to_DDS(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDS"
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'NA' на 'DDS'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_NA_to_DDR(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDR"
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'NA' на 'DDR'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DDR_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/4/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DDR' на 'NA'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DDS_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/5/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DDS' на 'NA'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DONE_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DONE' на 'NA','DDR','DDS','IP'"""


    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DONE_to_DDS(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "DDS"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DONE' на 'NA','DDR','DDS','IP'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DONE_to_DDR(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "DDR"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DONE' на 'NA','DDR','DDS','IP'"""

    @pytest.mark.django_db
    def test_views_update_order_with_wrong_status_DONE_to_IP(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "IP"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.data["detail"] == """Нельзя изменить статус с 'DONE' на 'NA','DDR','DDS','IP'"""

    @pytest.mark.django_db
    def test_views_update_order_with_cook_client(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_dishes": [1]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["number"] == get_orders[0].number
        assert response.data["menu_dishes"] == [1]
        assert response.data["menu_drinks"] == [1]
        assert response.data["waiter"] == 2
        assert response.data["status"] == get_orders[0].status

    @pytest.mark.django_db
    def test_views_update_order_with_bartender_client(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_drinks": [2]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["number"] == get_orders[0].number
        assert response.data["menu_dishes"] == [1, 2]
        assert response.data["menu_drinks"] == [2]
        assert response.data["waiter"] == 2
        assert response.data["status"] == get_orders[1].status

    @pytest.mark.django_db
    def test_views_update_order_with_admin_client(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_dishes": [2],
        "menu_drinks": [2]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["number"] == get_orders[0].number
        assert response.data["menu_dishes"] == [2]
        assert response.data["menu_drinks"] == [2]
        assert response.data["waiter"] == 2
        assert response.data["status"] == get_orders[1].status

    @pytest.mark.django_db
    def test_views_update_order_with_guest_client(self):
        guest_client = APIClient()
        data = {
        "waiter": 2,
        "menu_dishes": [1],
        "menu_drinks": [1]
        }
        response = guest_client.patch('/api/orders/1/', data=data, format='json')
        assert response.data["detail"] == "Чтобы редактировать заказ, вы должны быть авторизованы."

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_waiter_in_order(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/3/', data=data, format='json')
        response = authenticated_client.get('/api/orders/3/')
        assert response.data["table_number"] == get_orders[2].number
        assert response.data["dishes"] == []
        assert response.data["drinks"] == [2]
        assert response.data["waiter"] == 2
        assert response.data["status"] == "IP"

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_waiter_in_list_orders(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/3/', data=data, format='json')
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)
        assert response.data[2]["number"] == get_orders[2].number
        assert response.data[2]["waiter"] == 2
        assert response.data[2]["status"] == "IP"
        assert response.data[2]["menu_dishes"] == []
        assert response.data[2]["menu_drinks"] == [2]

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_admin_in_order(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/3/', data=data, format='json')
        response = authenticated_client.get('/api/orders/3/')
        assert response.data["table_number"] == get_orders[2].number
        assert response.data["dishes"] == []
        assert response.data["drinks"] == [2]
        assert response.data["waiter"] == 2
        assert response.data["status"] == "IP"

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_admin_in_list_orders(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/3/', data=data, format='json')
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == len(get_orders)
        assert response.data[2]["number"] == get_orders[2].number
        assert response.data[2]["waiter"] == 2
        assert response.data[2]["status"] == "IP"
        assert response.data[2]["menu_dishes"] == []
        assert response.data[2]["menu_drinks"] == [2]

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_cook_in_order(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/1/', data=data, format='json')
        response = authenticated_client.get('/api/orders/1/')
        assert response.data["table_number"] == get_orders[0].number
        assert response.data["dishes"] == [1, 2]
        assert response.data["status"] == "IP"
        assert response.data["comment"] == get_orders[0].comment

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_cook_in_list_orders(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/1/', data=data, format='json')
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 7
        assert response.data[0]["number"] == get_orders[0].number
        assert response.data[0]["status"] == "IP"
        assert response.data[0]["menu_dishes"] == [1, 2]
        assert response.data[0]["comment"] == get_orders[0].comment

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_bartender_in_order(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/1/', data=data, format='json')
        response = authenticated_client.get('/api/orders/1/')
        assert response.data["table_number"] == get_orders[0].number
        assert response.data["drinks"] == [1]
        assert response.data["status"] == "IP"
        assert response.data["comment"] == get_orders[0].comment

    @pytest.mark.django_db
    def test_views_update_order_and_get_list_by_bartender_in_list_orders(self, get_users, get_orders):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "IP"
        }
        authenticated_client.patch('/api/orders/1/', data=data, format='json')
        response = authenticated_client.get('/api/orders/')
        assert len(response.data) == 7
        assert response.data[0]["number"] == get_orders[0].number
        assert response.data[0]["status"] == "IP"
        assert response.data[0]["menu_drinks"] == [1]
        assert response.data[0]["comment"] == get_orders[0].comment