from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def catalog_view(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'categories': categories,
        'products': products,
        'current_category': category,
    }
    return render(request, 'catalog.html', context)
