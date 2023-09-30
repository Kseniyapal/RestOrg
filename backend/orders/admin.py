from django.contrib.admin import ModelAdmin, register

from .models import MenuItemDish, MenuItemDrink, Order


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('pk', 'number', 'comment')


@register(MenuItemDish)
class MenuItemDishAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'weight', 'price')


@register(MenuItemDrink)
class MenuItemDrinkAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'volume', 'price')
