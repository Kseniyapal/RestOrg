from orders.models import MenuItemDish
import pytest


@pytest.fixture(scope='session')
def get_dishes(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        MenuItemDish.objects.get_or_create({
        'id': 1,
        'name': 'Салат винегрет',
        'image' : 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
        'weight' : 180,
        'price' : 79
        })
        return MenuItemDish.objects.all()
    

@pytest.fixture(scope='session')
def get_dish(get_dishes):
    return get_dishes[0]