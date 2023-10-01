from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

NOT_ACTIVE = 'NA'
IN_PROCESS = 'IP'
DONE_DISH = 'DDS'
DONE_DRINK = 'DDR'

STATUS_CHOICES = (
    (NOT_ACTIVE, 'Not Active'),
    (IN_PROCESS, 'In Process'),
    (DONE_DISH, 'The dishes are ready'),
    (DONE_DRINK, 'The drinks are ready')
)


class MenuItemDish(models.Model):
    name = models.CharField(
        'Наименование блюда',
        max_length=255
    )
    image = models.ImageField(
        'фото блюда',
        upload_to='images/')
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
    image = models.ImageField(
        'Фото напитка',
        upload_to='images/')
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

    waiter = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='waiter',
                               blank=True,
                               null='')
    status = models.CharField(
        'Статус', max_length=3, choices=STATUS_CHOICES, default='NA'
    )

    """def clean(self):
        if (((self.status == 'DDS' or self.status == 'DDR')
            and self.pk
            and self.__class__.objects.filter(pk=self.pk, status='NA').exists()
            ) or ((self.status == 'NA')
            and self.pk
            and (self.__class__.objects.filter(pk=self.pk, status='DDS').exists() or
                 self.__class__.objects.filter(pk=self.pk, status='DDR').exists()))
            ):
            raise ValidationError("Cannot change status")"""
