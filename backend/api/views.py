from django_filters.rest_framework import DjangoFilterBackend
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (MenuItemDishSerializer, MenuItemDrinkSerializer,
                          OrderSerializer,  UserGetSerializer)
from djoser.views import UserViewSet
from users.models import User
from .filters import OrderFilter


class OrderViewSet(ModelViewSet):
    """Вьюсет для ингредиентов"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]


class MenuItemDrinkViewSet(ModelViewSet):
    """Вьюсет для ингредиентов"""

    queryset = MenuItemDrink.objects.all()
    serializer_class = MenuItemDrinkSerializer
    filter_backends = (DjangoFilterBackend,)


class MenuItemDishViewSet(ModelViewSet):
    """Вьюсет для ингредиентов"""

    queryset = MenuItemDish.objects.all()
    serializer_class = MenuItemDishSerializer
    filter_backends = (DjangoFilterBackend,)


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователей"""

    queryset = User.objects.all()
    serializer_class = UserGetSerializer
