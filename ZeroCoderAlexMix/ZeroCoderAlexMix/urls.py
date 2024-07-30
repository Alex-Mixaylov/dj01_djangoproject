from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Главная страница для приложения main
    path('data/', include('dz01_dj01.urls')),  # Страница для приложения dz01_dj01
    path('test/', include('dz01_dj01.urls')),  # Тоже страница для приложения dz01_dj01
]
