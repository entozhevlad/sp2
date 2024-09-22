from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'main'

urlpatterns = [
    path('', cache_page(60 * 15)(HomePageView.as_view()), name='home'),
    path('price/', service_view, name='price'),
]
