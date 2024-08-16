from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),
    path('catalog/category/<slug:category_slug>/', catalog_view, name='catalog_by_category'),
    path('catalog/<int:product_id>/', product_detail, name='product_detail'),

]
