# Generated by Django 4.0 on 2023-11-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_waiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemdish',
            name='image',
            field=models.CharField(max_length=500, verbose_name='фото блюда'),
        ),
        migrations.AlterField(
            model_name='menuitemdrink',
            name='image',
            field=models.CharField(max_length=500, verbose_name='Фото напитка'),
        ),
    ]
