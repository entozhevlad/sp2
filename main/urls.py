from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('price/', service_view, name='price'),
]
