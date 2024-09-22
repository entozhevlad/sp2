from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Service, Category, NewsImage
from catalog.models import Color, Product, ProductVariant, ProductCategory
from contacts.models import Adress
import environ
from django.db.models import Q
from django.contrib.admin.sites import site
from django.conf import settings
from django.views.decorators.cache import cache_page

env = environ.Env()

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_images'] = NewsImage.objects.all()

        return context


def catalog_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'services': services})


def service_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()

    for service in services:
        service.price_display = f'{int(service.price)}'

    return render(request, 'price.html', {'categories': categories, 'services': services})

def page_not_found(request, exception):
    return render(request, f'{settings.ERRORS_TEMPLATES_PATH}/404.html', status=404)

def internal_server_error(request):
    return render(request, f'{settings.ERRORS_TEMPLATES_PATH}/500.html', status=500)