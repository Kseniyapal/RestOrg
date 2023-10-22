import json

from django.core.management.base import BaseCommand

from orders.models import MenuItemDrink


class Command(BaseCommand):
    """Management команда для загрузки данных из json файла"""

    def handle(self, *args, **options):
        file_path = 'drinks.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for drink in data['drinks']:
            item_drink = MenuItemDrink.objects.create(
                name = drink['name'],
                image = drink['image'][28:],
                volume = int(drink['weight'][:-2]),
                price = int(drink['price'][:-4])
            )

        self.stdout.write(self.style.SUCCESS('Drinks loaded successfully'))