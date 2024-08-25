from django import forms
from main.models import Category, Service
from catalog.models import Color, ProductCategory, Product, ProductVariant
from contacts.models import Adress
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'price', 'is_visible']

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'image']

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'slug']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'description', 'material', 'additional_details',
            'height', 'size', 'density', 'diameter', 'application_method', 'volume'
        ]

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = [
            'product', 'name', 'color', 'price', 'main_image',
            'additional_image_1', 'additional_image_2', 'additional_image_3'
        ]

class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['adress', 'graphic_1', 'graphic_2']