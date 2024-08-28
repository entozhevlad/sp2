from django.shortcuts import render, get_object_or_404
from .models import ProductVariant, ProductCategory

def catalog_view(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    variants = ProductVariant.objects.all()  # Выбираем все варианты продуктов

    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        variants = variants.filter(product__category=category)  # Фильтруем варианты по категории продукта


    context = {
        'categories': categories,
        'variants': variants,  # Передаем варианты в контекст
        'current_category': category,
    }
    return render(request, 'catalog.html', context)


import random


def product_detail(request, product_id):
    product = get_object_or_404(ProductVariant, id=product_id)
    other_variants = ProductVariant.objects.filter(
        product=product.product
    ).exclude(id=product.id)



    # Выбираем случайные продукты для блока "ЕЩЕ"
    random_products = list(
        ProductVariant.objects.exclude(id=product.id).order_by('?')[:10])  # Например, 4 случайных продукта

    for variant in random_products:
        variant.price_display = int(variant.price)

    context = {
        'product': product,
        'other_variants': other_variants,  # Передаем другие варианты в контекст
        'random_products': random_products,  # Передаем случайные продукты в контекст
    }
    return render(request, 'product_detail.html', context)
