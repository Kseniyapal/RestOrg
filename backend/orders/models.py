from django.db import models
from users.models import User


class MenuItemDish(models.Model):
    name = models.CharField(
        'Наименование блюда',
        max_length=255
    )
    weight = models.IntegerField(
        'Вес в граммах')

    price = models.IntegerField(
        'Цена'
    )


class MenuItemDrink(models.Model):
    name = models.CharField(
        'Наименование напитка',
        max_length=255
    )
    volume = models.IntegerField(
        'Объем в мл')

    price = models.IntegerField(
        'Цена'
    )

class Order(models.Model):
    number = models.IntegerField(
        'Номер столика'
    )

    comment = models.CharField(
        'Комментарий', 
        max_length=255,
        blank=True
    )

    menu_dishes = models.ManyToManyField(MenuItemDish,)

    menu_drink = models.ManyToManyField(MenuItemDrink)

    waiter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='waiter')