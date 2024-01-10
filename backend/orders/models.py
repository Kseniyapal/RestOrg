"""Models for orders"""

from django.db import models
from users.models import User

NOT_ACTIVE = 'NA'
IN_PROCESS = 'IP'
DONE_DISH = 'DDS'
DONE_DRINK = 'DDR'
DONE = 'DONE'

STATUS_CHOICES = (
    (NOT_ACTIVE, 'Not Active'),
    (IN_PROCESS, 'In Process'),
    (DONE_DISH, 'The dishes are ready'),
    (DONE_DRINK, 'The drinks are ready')
)


class MenuItemDish(models.Model):
    """Class for item dish"""

    name = models.CharField(
        'Наименование блюда',
        max_length=255
    )
    image = models.CharField(
        'фото блюда',
        max_length=500)
    weight = models.IntegerField(
        'Вес в граммах')

    price = models.IntegerField(
        'Цена'
    )


class MenuItemDrink(models.Model):
    """Class for item drink"""

    name = models.CharField(
        'Наименование напитка',
        max_length=255
    )
    image = models.CharField(
        'Фото напитка',
        max_length=500)
    volume = models.IntegerField(
        'Объем в мл')

    price = models.IntegerField(
        'Цена'
    )


class Order(models.Model):
    """Class for order"""

    number = models.IntegerField(
        'Номер столика'
    )
    comment = models.CharField(
        'Комментарий',
        max_length=10000,
        blank=True
    )
    menu_dishes = models.ManyToManyField(MenuItemDish)
    menu_drinks = models.ManyToManyField(MenuItemDrink)
    waiter = models.ForeignKey(User, on_delete=models.CASCADE,
                               limit_choices_to={'role': 'W'},
                               related_name='waiter',
                               default=None,
                               null=True,
                               blank=True,
                               )
    status = models.CharField(
        'Статус', max_length=4, choices=STATUS_CHOICES, default='NA'
    )

    def get_drinks(self):
        """Return all drinks"""
        return self.menu_drinks

    def get_dishes(self):
        """Return all dishes"""
        return self.menu_dishes

    class Meta:
        """Class Meta"""
        ordering = ('id',)
