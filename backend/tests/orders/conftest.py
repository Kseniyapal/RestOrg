from orders.models import Order, MenuItemDish, MenuItemDrink
import pytest


@pytest.fixture(scope='session')
def get_orders(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        """Order.objects.get_or_create({
        'number' : 1,
        'menu_dishes' : MenuItemDish.set(1, 2),
        'menu_drinks' : [1],
        'waiter' : None
        })"""
        menu_dishes = MenuItemDish.objects.filter(id__in=[1, 2])
        menu_drinks = MenuItemDrink.objects.filter(id__in=[1])
        order, created = Order.objects.get_or_create(
        number=1,
        waiter=None,
        comment='',
        status='NA'
        )
        order.menu_dishes.set(menu_dishes)
        order.menu_drinks.set(menu_drinks)
        print(order.menu_drinks)
        return Order.objects.all()


@pytest.fixture(scope='session')
def get_order(get_orders, django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return get_orders[0]