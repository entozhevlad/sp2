from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'main'
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('b2b/', B2BPageView.as_view(), name='b2b'),
    path('us/',USPageView.as_view(), name='us'),
    path('price/', service_view, name='price')
]
