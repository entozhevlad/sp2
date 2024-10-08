from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),
    path('catalog/category/<slug:category_slug>/', catalog_view, name='catalog_by_category'),
    path('catalog/<slug:slug>/', product_detail, name='product_detail'),

]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)