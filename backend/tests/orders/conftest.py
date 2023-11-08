from orders.models import Order, MenuItemDish, MenuItemDrink
import pytest


@pytest.fixture(scope='session')
def get_orders(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        menu_dish = MenuItemDish.objects.create(
            id=12345678,
            name='Салат винегрет',
            image='http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
            weight=180,
            price=79
        )
        order = Order.objects.create(number=1234567)
        order.menu_dishes.add(menu_dish)
        return Order.objects.all()
    
@pytest.fixture(scope='session')
def get_order(get_orders, django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        response_data = {'number': get_orders[0].number}
        return get_orders.first()