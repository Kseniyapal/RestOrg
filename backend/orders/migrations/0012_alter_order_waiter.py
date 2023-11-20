# Generated by Django 4.0 on 2023-11-18 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_role'),
        ('orders', '0011_alter_menuitemdish_image_alter_menuitemdrink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(blank=True, default=None, limit_choices_to={'role': 'W'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waiter', to='users.user'),
        ),
    ]
