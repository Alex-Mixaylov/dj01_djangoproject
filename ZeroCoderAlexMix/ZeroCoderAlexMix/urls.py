from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),  # Маршруты для main с префиксом main/
    path('dz01_dj01/', include('dz01_dj01.urls')),  # Маршруты для dz01_dj01 с префиксом dz01_dj01/
]
