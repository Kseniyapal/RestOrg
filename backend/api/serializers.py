from djoser.serializers import UserCreateSerializer
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.serializers import ModelSerializer, IntegerField, ListSerializer, PrimaryKeyRelatedField, ListField
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

class UserGetSerializer(UserCreateSerializer):
    """Сериализатор получения пользователя"""
    class Meta:
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'role')
        model = User

class OrderSerializer(ModelSerializer):
    """Сериализер для """
    #waiter = IntegerField()
    #menu_dishes = ListField(child = IntegerField())
    #menu_drinks = ListField(child = IntegerField())
    waiter = UserGetSerializer(required=False)
    menu_dishes = MenuItemDishSerializer(many=True)
    menu_drinks = MenuItemDrinkSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'



