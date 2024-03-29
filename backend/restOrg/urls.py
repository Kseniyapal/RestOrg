"""Start urls"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('', views.index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
