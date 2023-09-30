from djoser.serializers import UserCreateSerializer
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.serializers import ModelSerializer
from users.models import User


class MenuItemDrinkSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDrink
        fields = '__all__'


class MenuItemDishSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = MenuItemDish
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    """Сериализер для """

    class Meta:
        model = Order
        fields = '__all__'


class UserGetSerializer(UserCreateSerializer):
    """Сериализатор получения пользователя"""
    class Meta:
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'role')
        model = User

