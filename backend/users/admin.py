"""Settings admin"""

from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import User


@register(User)
class MyUserAdmin(UserAdmin):
    """Class for fields in admin site"""
    list_display = ('pk',
                    'email',
                    'first_name',
                    'last_name',
                    'role')
