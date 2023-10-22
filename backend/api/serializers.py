from djoser.serializers import UserCreateSerializer
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import User


class MenuItemDrinkSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDrink
        fields = ('id', 'name')


class MenuItemDishSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDish
        fields = ('id', 'name', 'image')


class UserGetSerializer(UserCreateSerializer):
    """Сериализатор получения пользователя"""
    class Meta:
        model = User
        fields = '__all__'
     

class OrderSerializer(ModelSerializer):
    """Сериализер для """
    waiter = PrimaryKeyRelatedField(allow_null=True, required = False, queryset=User.objects.all())
    menu_dishes = PrimaryKeyRelatedField(many=True,
                                         queryset=MenuItemDish.objects.all())
    menu_drinks = PrimaryKeyRelatedField(many=True,
                                         queryset=MenuItemDrink.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'number','waiter', 'menu_dishes', 'menu_drinks']



