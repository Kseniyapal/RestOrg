from orders.models import MenuItemDrink
import pytest


@pytest.fixture(scope='session')
def get_drinks(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        MenuItemDrink.objects.get_or_create({
        "id": 1,
        "name":"Лимонад натуральный с мятой",
        "image" : "http://127.0.0.1:8000/media/images/Limonad-s-myatoj-500x350-1200x800.jpg",
        "volume" : 250,
        "price" : 59
        })
        return MenuItemDrink.objects.all()
    

@pytest.fixture(scope='session')
def get_drink(get_dishes):
    return get_dishes[0]