from users.models import User
from orders.models import MenuItemDish, MenuItemDrink
import pytest


example_list_dishes = [[1, 'Салат', 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg', 100, 5],
        [2,'Салат из свежих овощей', 'http://127.0.0.1:8000/media/images/821f70dc9e49e8f0c0c92f7dbef1f12b.jpeg', 200, 149]]

@pytest.mark.django_db
def create_dish():
    MenuItemDish.objects.get_or_create({
    'id': 1,
    'name': 'Салат винегрет',
    'image' : 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
    'weight' : 180,
    'price' : 79
    })
    return MenuItemDish.objects.all()

dishes = create_dish()

@pytest.fixture
def get_dishes():
    return dishes

@pytest.fixture
def get_dish():
    return dishes[0]