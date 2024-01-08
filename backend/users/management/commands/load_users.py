"""File for load users"""

import json

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Management команда для загрузки данных из json файла"""

    def handle(self, *args, **options):
        file_path = 'users.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for user in data['users']:
            item_user = User.objects.create(
                username=user['username'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                role=user['role'],
                email=user['email'],
                password=user['password']
            )
            item_user.set_password(user['password'])
            item_user.save()
        self.stdout.write(self.style.SUCCESS('Users loaded successfully'))
