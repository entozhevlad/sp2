from django.urls import path
from .views import *
app_name = 'contacts'
urlpatterns = [
    path('contacts/', address_view, name='contacts'),

]
