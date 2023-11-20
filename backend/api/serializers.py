from djoser.serializers import UserCreateSerializer 
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ImageField
from users.models import User
import base64
from django.core.files.base import ContentFile


class Base64ImageField(ImageField):
    """Кастомное поле для кодирования изображения в base64."""

    def to_internal_value(self, data):
        """Метод преобразования картинки"""

        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='photo.' + ext)

        return super().to_internal_value(data)

class MenuItemDrinkSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDrink
        fields = ['id', 'name', 'image', 'volume', 'price']


class MenuItemDishSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDish
        fields = ['name', 'image', 'weight', 'price']


class UserGetSerializer(ModelSerializer):
    """Сериализатор получения пользователя"""
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ['password']
    

class OrderSerializer(ModelSerializer):
    """Сериализер для """
    waiter = PrimaryKeyRelatedField(allow_null=True, required = False, queryset=User.objects.all())
    menu_dishes = PrimaryKeyRelatedField(many=True,
                                         queryset=MenuItemDish.objects.all())
    menu_drinks = PrimaryKeyRelatedField(many=True,
                                         queryset=MenuItemDrink.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'number','waiter', 'menu_dishes', 'menu_drinks', 'status', 'comment']



