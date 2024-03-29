# Generated by Django 3.2.16 on 2023-10-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20231015_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu_dishes',
            field=models.ManyToManyField(null=True, to='orders.MenuItemDish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='menu_drinks',
            field=models.ManyToManyField(null=True, to='orders.MenuItemDrink'),
        ),
    ]
