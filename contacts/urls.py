from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'contacts'
urlpatterns = [
    path('b2b/', contact_view, name='b2b'),
    path('success/', success_view, name='success'),

]
