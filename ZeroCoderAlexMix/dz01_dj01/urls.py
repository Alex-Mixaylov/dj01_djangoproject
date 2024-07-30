from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dz01_dj01_index'),  # Главная страница для dz01_dj01
    path('data/', views.data, name='dz01_dj01_data'),  # Страница data для dz01_dj01
    path('test/', views.test, name='dz01_dj01_test'),  # Страница test для dz01_dj01
]
