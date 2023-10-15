from django.contrib.auth.models import AbstractUser
from django.db import models

WAITER = 'W'
COOK = 'C'
BARTENDER = 'B'
ADMIN = 'A'

ROLE_CHOICES = (
    (WAITER, 'Waiter'),
    (COOK, 'Cook'),
    (BARTENDER, 'Bartender'),
    (ADMIN, 'Admin')
    ) 


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
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'role']

    def save(self, *args, **kwargs):
        if self.role == 'A':
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
