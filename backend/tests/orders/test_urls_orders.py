from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish, MenuItemDrink
import pytest

class TestUrlsOrders():

    """@pytest.mark.django_db
    def test_get_list_orders_with_guest_client(self, get_orders):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/')
        assert response.status_code == 401"""

    @pytest.mark.django_db
    def test_get_list_orders_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/orders/')
        assert response.status_code == 200

    """@pytest.mark.django_db
    def test_get_order_with_guest_client(self, get_orders):
        guest_client = APIClient()
        response = guest_client.get('/api/orders/1/')
        assert response.status_code == 401"""

    @pytest.mark.django_db
    def test_get_order_with_authorized_client(self, get_orders):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        print(get_orders[0])
        response = client.get(f'/api/orders/{get_orders[0].id}/')
        
        assert response.status_code == 200
        
