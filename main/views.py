from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class PricePageView(TemplateView):
    template_name = 'price.html'
class ContactsPageView(TemplateView):
    template_name='contacts.htm;'
