# Generated by Django 4.0 on 2023-10-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
        ('orders', '0007_alter_order_waiter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='waiter', to='users.user'),
        ),
    ]