from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.product_list, name='product_list'),  # Главная страница каталога
    path('catalog/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),  # Фильтр по категориям
]
