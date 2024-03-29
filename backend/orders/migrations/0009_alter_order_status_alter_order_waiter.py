# Generated by Django 4.0 on 2023-10-22 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
        ('orders', '0008_alter_order_options_alter_order_waiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NA', 'Not Active'), ('IP', 'In Process'), ('DDS', 'The dishes are ready'), ('DDR', 'The drinks are ready')], default='NA', max_length=4, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='waiter', to='users.user'),
        ),
    ]
