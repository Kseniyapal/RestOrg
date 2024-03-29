# Generated by Django 4.0 on 2023-10-22 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
        ('orders', '0009_alter_order_status_alter_order_waiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(blank=True, default=None, limit_choices_to={'role': 'W'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='waiter', to='users.user'),
        ),
    ]
