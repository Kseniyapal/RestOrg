from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish, MenuItemDrink
import pytest

class TestUrlsOrders():

    @pytest.mark.django_db
    def test_get_list_orders_with_guest_client(self, get_orders):
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

    @pytest.mark.django_db
    def test_get_order_with_guest_client(self, get_orders):
        guest_client = APIClient()
        response = guest_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_order_with_waiter_client(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_order_with_guest_client(self):
        guest_client = APIClient()
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        response = guest_client.post('/api/orders/', data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_order_with_waiter_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "menu_dishes": [1],
        "menu_drinks": [1],
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_order_with_bartender_client(self, get_users):
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
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_order_with_cook_client(self, get_users):
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
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_order_with_admin_client(self, get_users):
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
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_order_with_no_waiter(self, get_users):
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
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_order_without_dishes_drinks_(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "number": 101,
        "waiter": 2
        }
        response = authenticated_client.post('/api/orders/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_waiter_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_update_order_with_no_waiter_data(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 3
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_NA_to_DDR(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDR"
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_NA_to_DDS(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDS"
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_NA_to_DDR(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDR"
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DDR_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/4/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DDS_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/5/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DONE_to_NA(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "NA"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DONE_to_DDS(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDS"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DONE_to_DDR(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "DDR"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_wrong_status_DONE_to_IN(self, get_users):
        authenticated_client = APIClient()
        user = get_users[1]
        authenticated_client.force_authenticate(user=user)
        data = {
        "status": "IN"
        }
        response = authenticated_client.patch('/api/orders/6/', data=data, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_order_with_cook_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_dishes": [1]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_order_with_bartender_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_drinks": [1]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_order_with_admin_client(self, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        data = {
        "waiter": 2,
        "menu_dishes": [1],
        "menu_drinks": [1]
        }
        response = authenticated_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_order_with_guest_client(self):
        guest_client = APIClient()
        data = {
        "waiter": 2,
        "menu_dishes": [1],
        "menu_drinks": [1]
        }
        response = guest_client.patch('/api/orders/1/', data=data, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_get_order_with_empty_dishes_by_cook(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[2].id}/')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_get_order_with_dishes_by_cook(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[2]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[1].id}/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_order_with_empty_drinks_by_bartender(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[1].id}/')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_get_order_with_drinks_by_bartender(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[0]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_order_with_drinks_by_admin(self, get_orders, get_users):
        authenticated_client = APIClient()
        user = get_users[3]
        authenticated_client.force_authenticate(user=user)
        response = authenticated_client.get(f'/api/orders/{get_orders[0].id}/')
        assert response.status_code == 200

    