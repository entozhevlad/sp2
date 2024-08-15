from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Service, Category
from django.core.mail import send_mail
from django.conf import settings
from contacts.forms import ContactForm
import environ

env = environ.Env()


class HomePageView(TemplateView):
    template_name = 'home.html'


def catalog_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'services': services})


def service_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()
    return render(request, 'price.html', {'categories': categories, 'services': services})
