from django.db import models
from users.models import User


class MenuItem(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=255
    )

    price = models.IntegerField(
        'Цена'
    )


class Menu(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)


class Order(models.Model):
    number = models.IntegerField(
        'Номер столика'
    )

    comment = models.CharField(
        'Комментарий', 
        max_length=255,
        blank=True
    )

    menu_dishes = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name='menu_dishes')

    menu_drink = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name='menu_drink')

    waiter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='waiter')