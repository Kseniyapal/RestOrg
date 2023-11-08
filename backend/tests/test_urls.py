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


 