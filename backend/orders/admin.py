from django.contrib.admin import ModelAdmin, register
from .models import Order,Menu,MenuItem


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('pk', 'number', 'comment')

@register(Menu)
class MenuAdmin(ModelAdmin):
    pass

@register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'price')