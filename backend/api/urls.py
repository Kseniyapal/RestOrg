"""API urls"""

from django.urls import include, path
from rest_framework import routers

from .views import (MenuItemDishViewSet, MenuItemDrinkViewSet, OrderViewSet,
                    UserViewSet)

APP_NAME = 'api'

router = routers.DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('dishes', MenuItemDishViewSet,  basename='dishes')
router.register('drinks', MenuItemDrinkViewSet,  basename='drinks')
router.register('users', UserViewSet,  basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
