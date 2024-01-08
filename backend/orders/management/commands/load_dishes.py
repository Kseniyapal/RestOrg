"""File for load dishes"""

import json

from django.core.management.base import BaseCommand

from orders.models import MenuItemDish


class Command(BaseCommand):
    """Management команда для загрузки данных из json файла"""

    def handle(self, *args, **options):
        file_path = 'dishes.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for dish in data['dishes']:
            MenuItemDish.objects.create(
                name=dish['name'],
                image=dish['image'][28:],
                weight=int(dish['weight'][:-1]),
                price=int(dish['price'][:-4])
            )

        self.stdout.write(self.style.SUCCESS('Dishes loaded successfully'))
