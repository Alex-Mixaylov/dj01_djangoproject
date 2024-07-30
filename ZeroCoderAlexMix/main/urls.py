from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),  # Главная страница для main
    path('new/', views.new, name='main_new'),  # Страница new для main
]
