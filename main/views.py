from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Service, Category, NewsImage, WorkExample
import environ
from django.conf import settings
from django.views.decorators.cache import cache_page

env = environ.Env()

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_images'] = NewsImage.objects.all()
        context['work_examples'] = WorkExample.objects.all()[:10]  # Ограничение на 10 фото

        return context

@cache_page(60 * 5)
def service_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()

    for service in services:
        service.price_display = f'{int(service.price)}'

    return render(request, 'price.html', {'categories': categories, 'services': services})

@cache_page(60 * 5)
def page_not_found(request, exception):
    return render(request, f'{settings.ERRORS_TEMPLATES_PATH}/404.html', status=404)

@cache_page(60 * 5)
def internal_server_error(request):
    return render(request, f'{settings.ERRORS_TEMPLATES_PATH}/500.html', status=500)