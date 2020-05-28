from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django_with_PostgreSQL_app.views import ListWaterLevelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_with_PostgreSQL_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
