from orders.models import Order, MenuItemDrink, MenuItemDish
from users.models import User
import pytest


@pytest.fixture(scope='session')
def get_drinks(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        MenuItemDrink.objects.bulk_create([
            MenuItemDrink(
        id= 1,
        name= "Лимонад натуральный с мятой",
        image= "http://127.0.0.1:8000/media/images/Limonad-s-myatoj-500x350-1200x800.jpg",
        volume= 250,
        price= 59
        ),
        MenuItemDrink(
        id= 2,
        name= "Лимонад натуральный без мяты",
        image= "http://127.0.0.1:8000/media/images/Limonad-s-myatoj-500x350-1200x800.jpg",
        volume= 250,
        price= 79
        )
        ])
        return MenuItemDrink.objects.all()


@pytest.fixture(scope='session')
def get_users(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        users = User.objects.bulk_create([
            User(
                id=1,
                username='Vanya',
                first_name='Vanya',
                last_name='Ivanov',
                role='B',
                email='ivan@ivan.ru',
                #password='1234dfghjmk,l'
            ),
            User(
                id=2,
                username='Petya',
                first_name='Petya',
                last_name='Ivanov',
                role='W',
                email='petr@petr.ru',
                password='1234sxdcfvgbhjk'
            ),
            User(
                id=3,
                username='Senya',
                first_name='senya',
                last_name='Samsonov',
                role='C',
                email='semen@semen.ru',
                password='1234sxdcfvgbhnjmk'
            ),
            User(
                id=4,
                username='adminn',
                first_name='adminn',
                last_name='adminn',
                role='A',
                is_superuser= True,
                is_staff= True,
                is_active= True,
                email='ad@ad.ru',
                password='1234decfvgbhnjm'
            )
        ])
        user = User.objects.get(id=1)
        user.set_password('1234dfghjmk,l')
        user.save()
        return User.objects.all()


@pytest.fixture(scope='session')
def get_dishes(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        MenuItemDish.objects.bulk_create([
            MenuItemDish(
                id=1,
                name='Салат винегрет',
                image='http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
                weight=180,
                price=79
            ),
        MenuItemDish(
                id=2,
                name='Салат домашний винегрет',
                image='http://127.0.0.1:8000/media/images/salat-vinegret.jpg',
                weight=280,
                price=790
            )
        ])
        return MenuItemDish.objects.all()
    
@pytest.fixture(scope='session')
def get_orders(get_users, get_dishes, get_drinks, django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        order = Order.objects.create(number=1234567,  waiter=get_users[1])
        order.menu_dishes.add(get_dishes[0])
        order.menu_drinks.add(get_drinks[0])
        

        order = Order.objects.create(number=1234568, waiter=get_users[1])
        order.menu_dishes.add(get_dishes[1])

        order = Order.objects.create(number=1234569)
        order.menu_drinks.add(get_drinks[1])

        order = Order.objects.create(number=1234570, status='DDR')
        order.menu_dishes.add(get_dishes[0])
        order.menu_drinks.add(get_drinks[0])

        order = Order.objects.create(number=1234571, status='DDS')
        order.menu_dishes.add(get_dishes[0])
        order.menu_drinks.add(get_drinks[0])

        order = Order.objects.create(number=1234572, status='DONE')
        order.menu_dishes.add(get_dishes[0])
        order.menu_drinks.add(get_drinks[0])
        
        return Order.objects.all()
    
    