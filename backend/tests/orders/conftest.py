from orders.models import Order, MenuItemDish, MenuItemDrink
import pytest


@pytest.fixture(scope='session')
def get_orders(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        menu = MenuItemDish.objects.get_or_create({
        'id': 1,
        'name': 'Салат винегрет',
        'image' : 'http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
        'weight' : 180,
        'price' : 79
        })
        menu_dishes_ids = [1]  
        menu_drinks_ids = []  
        menu_dishes = MenuItemDish.objects.filter(id__in=menu_dishes_ids)
        #order.menu_dishes.set(menu_dishes)
        menu_drinks = MenuItemDrink.objects.filter(id__in=menu_drinks_ids)
        #order.menu_drinks.set(menu_drinks)
        order_data = {
            'id': 1,
            'number': 1,
            'waiter': None,
            "menu_dishes": [1],
            "menu_drinks": menu_drinks
        }
        order, _ = Order.objects.get_or_create(**order_data)
        return Order.objects.all()
    
@pytest.fixture(scope='session')
def get_order(get_orders, django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        response_data = {'number': get_orders[0].number}
        return get_orders.first()