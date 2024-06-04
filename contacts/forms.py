from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше Имя')
    email = forms.EmailField(label='Ваш Email')
    phone = forms.CharField(max_length=15, label='Телефон', initial='+7')
    message = forms.CharField(widget=forms.Textarea, label='Опишите вашу проблему, и мы с вами свяжемся')
