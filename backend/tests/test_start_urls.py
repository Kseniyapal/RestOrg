from rest_framework.test import APIClient
import pytest


class TestStartUrls():

    @pytest.mark.django_db
    def test_start_page(self):
        guest_client = APIClient()
        response = guest_client.get('/')
        assert response.status_code == 200


 