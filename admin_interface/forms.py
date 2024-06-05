# forms.py
from django import forms
from main.models import Category, Service

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'price', 'is_visible']
