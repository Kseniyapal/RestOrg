from rest_framework.test import APIClient
from users.models import User
from orders.models import MenuItemDish, MenuItemDrink
import pytest


class TestUrls():

    @pytest.mark.django_db
    def test_start_page(self):
        guest_client = APIClient()
        response = guest_client.get('/')
        assert response.status_code == 200
   
    
    @pytest.mark.django_db
    def test_list_users_with_guest_client(self):
        guest_client = APIClient()
        response = guest_client.get('/api/users/')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_users_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/users/')
        assert response.status_code == 200

 