from django.shortcuts import render, redirect
import environ
from django.views.decorators.cache import cache_page

from .models import Adress

env = environ.Env()

@cache_page(60 * 5)
def address_view(request):
    addresses = Adress.objects.all()
    return render(request, 'contacts.html', {'addresses': addresses})

