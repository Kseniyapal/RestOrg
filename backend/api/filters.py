import django_filters
from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    waiter_id = django_filters.NumberFilter(
        field_name='waiter__id', label='Waiter ID')
    menu_dishes_empty = django_filters.BooleanFilter(
        field_name='menu_dishes', lookup_expr='isnull',
        exclude=True, label='Menu Dishes Empty')
    menu_drinks_empty = django_filters.BooleanFilter(
        field_name='menu_drinks',
        lookup_expr='isnull',
        exclude=True,
        label='Menu Drinks Empty')

    class Meta:
        model = Order
        fields = ['status',
                  'waiter_id',
                  'menu_dishes_empty',
                  'menu_drinks_empty']
