from users.models import User
import pytest


@pytest.fixture(scope='session')
def get_users(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        User.objects.bulk_create([
            User(
                id=1,
                username='Vanya',
                first_name='Vanya',
                last_name='Ivanov',
                role='B',
                email='ivan@ivan.ru',
                password=1234
            ),
            User(
                id=2,
                username='adminn',
                first_name='adminn',
                last_name='adminn',
                role='A',
                email='ad@ad.ru',
                password=1234
            )
        ])
        return User.objects.all()