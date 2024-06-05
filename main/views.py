from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Service, Category


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class B2BPageView(TemplateView):
    template_name = 'b2b.html'
class USPageView(TemplateView):
    template_name = 'us.html'
def service_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()
    return render(request, 'price.html', {'categories': categories, 'services': services})
