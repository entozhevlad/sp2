from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'contacts'
urlpatterns = [
    path('contacts/', contact_view, name='contacts'),
    path('success/', success_view, name='success'),

]
