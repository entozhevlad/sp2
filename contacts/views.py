from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import environ

from .models import Adress

env = environ.Env()



def contact_view(request):
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
    return render(request, 'contacts.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

def address_view(request):
    addresses = Adress.objects.all()
    return render(request, 'contacts.html', {'addresses': addresses})

