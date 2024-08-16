from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),  # Главная страница каталога
    path('catalog/category/<slug:category_slug>/', catalog_view, name='catalog_by_category'),
]
