from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from main.views import page_not_found, internal_server_error
app_name = 'main'

urlpatterns = [
    path('', cache_page(60)(HomePageView.as_view()), name='home'),
    path('price/', service_view, name='price'),
]

handler404 = page_not_found
handler500 = internal_server_error

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)