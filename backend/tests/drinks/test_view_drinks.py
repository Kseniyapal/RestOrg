from orders.models import MenuItemDrink
import pytest

class TestViewDrinks():
    @pytest.mark.django_db
    def test_create_item_drink(self):
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