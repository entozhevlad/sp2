from tempfile import template

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .sitemaps import *
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import handler404, handler500

sitemaps = {
    'products': ProductVariantSitemap,
    'product_category': ProductCategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('', include('contacts.urls')),
    path('', include('catalog.urls')),
    re_path(r'robots\.txt$', TemplateView.as_view(template_name="sp/robots.txt", content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}),
]
handler404 = 'main.views.page_not_found'
handler500 = 'main.views.internal_server_error'


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
