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


def product_detail(request, slug):
    product = get_object_or_404(ProductVariant, slug=slug)
    other_variants = ProductVariant.objects.filter(
        product=product.product
    ).exclude(id=product.id)

    random_products = list(
        ProductVariant.objects.exclude(id=product.id).order_by('?')[:10]
    )
    for variant in random_products:
        variant.price_display = int(variant.price)

    context = {
        'product': product,
        'other_variants': other_variants,
        'random_products': random_products,
    }
    return render(request, 'product_detail.html', context)

