from django_filters.rest_framework import DjangoFilterBackend
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (MenuItemDishSerializer, MenuItemDrinkSerializer,
                          OrderSerializer,  UserGetSerializer)
from djoser.views import UserViewSet
from users.models import User
from .filters import OrderFilter
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.exceptions import ValidationError


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

    def retrieve(self, request, *args, **kwargs):      
        obj = self.get_object()
        serializer = OrderSerializer(obj)
        role_user = request.user.role
        if role_user == 'B':
            data = {
            'drinks': serializer.data['menu_drinks'],
            'table_number': serializer.data['number'],
            'status': serializer.data['status'],
            }
            return Response(data, status=status.HTTP_200_OK)
        if role_user == 'W':
            data = {
            'dishes': serializer.data['menu_dishes'],    
            'drinks': serializer.data['menu_drinks'],
            'table_number': serializer.data['number'],
            'status': serializer.data['status'],
            'comment': serializer.data['comment'],
            }
            return Response(data, status=status.HTTP_200_OK)
        if role_user == 'C':
            data = {
            'dishes': serializer.data['menu_dishes'],
            'table_number': serializer.data['number'],
            'status': serializer.data['status'],
            }
            return Response(data, status=status.HTTP_200_OK)
        
    def list(self, request, *args, **kwargs):
        role_user = request.user.role
        if role_user == 'B':
            queryset = self.queryset.filter(menu_drinks__isnull=False)
            serializer = OrderSerializer(queryset, many = True)
        elif role_user == 'C':
            queryset = self.queryset.filter(menu_dishes__isnull=False)
            serializer = OrderSerializer(queryset, many = True)
        else:
            serializer = self.get_serializer(self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        menu_dishes = request.data.get('menu_dishes', [])
        menu_drinks = request.data.get('menu_drinks', [])

        if not menu_dishes and not menu_drinks:
            data = {
                'error' : "Заказ должен содержать хотя бы одно блюдо или напиток.",
                'form' : OrderSerializer(request.data).data
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'form' : OrderSerializer(request.data).data
        }
        return Response(data, status=status.HTTP_201_CREATED)

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
