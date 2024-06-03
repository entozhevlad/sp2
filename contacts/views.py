from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class ContactsPageView(TemplateView):
    template_name = 'contact.html'


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
                ['vaz30@tpu.ru'],  # Замените на фиксированный почтовый адрес
                fail_silently=False,
            )
            return redirect('main:home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')