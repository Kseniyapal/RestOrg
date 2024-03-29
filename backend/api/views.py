"""Views"""

from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from djoser.views import UserViewSet
from orders.models import MenuItemDish, MenuItemDrink, Order
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User
from .filters import OrderFilter
from .serializers import (MenuItemDishSerializer, MenuItemDrinkSerializer,
                          OrderSerializer, UserGetSerializer)


class OrderViewSet(ModelViewSet):
    """Вьюсет для заказов"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]

    def retrieve(self, request,  *args, **kwargs):
        obj = self.get_object()
        serializer = OrderSerializer(obj)
        role_user = request.user.role

        if role_user == 'B':
            if not serializer.data['menu_drinks']:
                raise PermissionDenied(
                   detail="У вас нет прав для просмотра этого заказа."
                )
            data = {
                   'drinks': serializer.data['menu_drinks'],
                   'table_number': serializer.data['number'],
                   'status': serializer.data['status'],
                   'comment': serializer.data['comment']
                   }
            return Response(data, status=status.HTTP_200_OK)

        if role_user == 'W' or role_user == 'A':
            data = {
                   'dishes': serializer.data['menu_dishes'],
                   'drinks': serializer.data['menu_drinks'],
                   'table_number': serializer.data['number'],
                   'status': serializer.data['status'],
                   'comment': serializer.data['comment'],
                   'waiter': serializer.data['waiter'],
                   'id': serializer.data['id']
                   }
            return Response(data, status=status.HTTP_200_OK)

        if role_user == 'C':
            if not serializer.data['menu_dishes']:
                raise PermissionDenied(
                    detail="У вас нет прав для просмотра этого заказа."
                )
            data = {
                   'dishes': serializer.data['menu_dishes'],
                   'table_number': serializer.data['number'],
                   'status': serializer.data['status'],
                   'comment': serializer.data['comment']
            }
            return Response(data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        role_user = request.user.role

        if role_user == 'B':
            self.queryset = self.queryset.filter(
                menu_drinks__isnull=False
            ).distinct()
        elif role_user == 'C':
            self.queryset = self.queryset.filter(
                menu_dishes__isnull=False
            ).distinct()
        else:
            self.queryset = Order.objects.all()

        serializer = OrderSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        data = serializer.validated_data
        menu_ds = self.request.data.get('menu_dishes', [])
        menu_dr = self.request.data.get('menu_drinks', [])
        order_waiter = self.request.data.get('waiter', )
        list_users = User.objects.filter(role='W').values_list('id', flat=True)
        if order_waiter is not None and order_waiter not in list_users:
            raise ValidationError(
                "Надо указать официанта исполнителем"
            )
        comment_res = self.request.data.get('comment', '')
        if (len(menu_dr) == 0 and len(menu_ds) == 0):
            raise ValidationError(
                "Нужно указать хотя бы одно блюдо или напиток в заказе"
            )
        serializer.save(number=data['number'],
                        comment=comment_res,
                        waiter=data['waiter'], menu_drinks=menu_dr,
                        menu_dishes=menu_ds)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        instance = serializer.instance
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied(
                "Чтобы редактировать заказ, вы должны быть авторизованы."
            )
        order_waiter = self.request.data.get('waiter', )
        db_order_waiter = Order.objects.get(id=instance.id).waiter
        list_users = User.objects.filter(role='W').values_list('id', flat=True)
        if ((order_waiter is None and db_order_waiter is None) or
                (order_waiter not in list_users and order_waiter is not None)):
            raise ValidationError("Надо указать официанта исполнителем")
        if (instance.status == 'NA' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'DDR'):
            raise PermissionDenied("Нельзя изменить статус с 'NA' на 'DDR'")
        if (instance.status == 'NA' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'DDS'):
            raise PermissionDenied("Нельзя изменить статус с 'NA' на 'DDS'")
        if (instance.status == 'DDS' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'DDR'):
            serializer.validated_data['status'] = 'DONE'
        if (instance.status == 'DDR' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'DDS'):
            serializer.validated_data['status'] = 'DONE'
        if (instance.status == 'DDR' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'NA'):
            raise PermissionDenied("Нельзя изменить статус с 'DDR' на 'NA'")
        if (instance.status == 'DDS' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] == 'NA'):
            raise PermissionDenied("Нельзя изменить статус с 'DDS' на 'NA'")
        if (instance.status == 'DONE' and 'status' in serializer.validated_data
                and serializer.validated_data['status'] in
                ['NA', 'DDR', 'DDS', 'IP']):
            raise PermissionDenied(
                "Нельзя изменить статус с 'DONE' на 'NA','DDR','DDS','IP'"
            )
        if (len(instance.menu_drinks.all()) == 0 and
                serializer.validated_data['status'] == 'DDS'):
            serializer.validated_data['status'] = 'DONE'
        if (len(instance.menu_dishes.all()) == 0 and
                serializer.validated_data['status'] == 'DDR'):
            serializer.validated_data['status'] = 'DONE'

        super().perform_update(serializer)
        self.queryset = Order.objects.all()


class MenuItemDrinkViewSet(ModelViewSet):
    """Вьюсет для напитков"""

    queryset = MenuItemDrink.objects.all()
    serializer_class = MenuItemDrinkSerializer
    filter_backends = (DjangoFilterBackend,)

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied(
                "Чтобы создать пункт меню, \
                     вы должны обладать правами администратора.")
        data = serializer.validated_data
        serializer.save(name=data['name'],
                        image=data['image'],
                        volume=data['volume'],
                        price=data['price'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        user = self.request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied("Чтобы редактировать пункт меню, \
                                    вы должны обладать правами администратора."
                                   )

        super().perform_update(serializer)


class MenuItemDishViewSet(ModelViewSet):
    """Вьюсет для блюд"""

    queryset = MenuItemDish.objects.all()
    serializer_class = MenuItemDishSerializer
    filter_backends = (DjangoFilterBackend,)

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied("Чтобы создать пункт меню, \
                                    вы должны обладать правами администратора."
                                   )
        data = serializer.validated_data
        serializer.save(name=data['name'],
                        image=data['image'],
                        weight=data['weight'],
                        price=data['price'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        user = self.request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied("Чтобы редактировать пункт меню, \
                                    вы должны обладать правами администратора."
                                   )

        super().perform_update(serializer)


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователей"""

    queryset = User.objects.all()
    serializer_class = UserGetSerializer


@require_http_methods(["GET"])
def index(request):
    """Return http response"""
    return HttpResponse(status=200)
