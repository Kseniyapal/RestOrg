from rest_framework.test import APIClient
from users.models import User
import pytest

class TestUrlsDishes():

    @pytest.mark.django_db
    def test_get_menu_dishes_with_guest_client(self, get_dishes):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/')
        assert response.status_code == 200
        #assert len(response.data) == 1
        #assert response.data[0]['id'] == get_dishes[0].id

    @pytest.mark.django_db
    def test_get_menu_dishes_with_authorized_client(self):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_authorized_client(self, get_dishes):
        client = APIClient()
        user = User.objects.create_user("John")
        client.force_authenticate(user=user)
        response = client.get('/api/dishes/1/')
        assert response.status_code == 200

    
    @pytest.mark.django_db
    def test_get_menu_item_dish_with_guest_client(self, get_dishes):
        guest_client = APIClient()
        response = guest_client.get('/api/dishes/1/')
        assert response.status_code == 200