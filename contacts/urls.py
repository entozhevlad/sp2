from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contacts'
urlpatterns = [
    path('contacts/', address_view, name='contacts'),

]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)