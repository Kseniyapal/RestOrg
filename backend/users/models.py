from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        unique=True,
        db_index=True
    )
    
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name='Отчество'
    )
    
    WAITER = 'W'
    COOK = 'C'
    BARTENDER = 'B'

    ROLE_CHOICES = (
    (WAITER, 'Waiter'),
    (COOK, 'Cook'),
    (BARTENDER, 'Bartender'),
    ) 

    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=BARTENDER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def str(self):
        return self.email