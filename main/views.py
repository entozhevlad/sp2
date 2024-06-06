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

def B2BPageView(request):
    template_name = 'b2b.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            full_message = f"Имя: {name}\nEmail: {email}\nТелефон: {phone}\n\nСообщение:\n{message}"

            send_mail(
                'Новое сообщение с сайта',
                full_message,
                settings.EMAIL_HOST_USER,
                [env('STATIC_EMAIL')],
                fail_silently=False,
            )
            return redirect('main:home')
    else:
        form = ContactForm()
    return render(request, template_name, {'form': form})

class USPageView(TemplateView):
    template_name = 'us.html'
def service_view(request):
    services = Service.objects.filter(is_visible=True)
    categories = Category.objects.all()
    return render(request, 'price.html', {'categories': categories, 'services': services})
