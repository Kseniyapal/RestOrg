"""Apps"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API Configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
