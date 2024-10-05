from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductVariant, ProductCategory
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def catalog_view(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    variants = ProductVariant.objects.select_related('product', 'color')

    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        variants = variants.filter(product__category=category)

    paginator = Paginator(variants, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'variants': page_obj,
        'current_category': category,
    }
    return render(request, 'catalog.html', context)

@cache_page(60 * 5)
def product_detail(request, slug):
    product = get_object_or_404(ProductVariant.objects.select_related('product', 'color'), slug=slug)
    other_variants = product.get_other_variants().select_related('color')

    random_products = list(
        ProductVariant.objects.select_related('product', 'color').exclude(id=product.id).order_by('?')[:10]
    )
    for variant in random_products:
        variant.price_display = int(variant.price)

    context = {
        'product': product,
        'other_variants': other_variants,
        'random_products': random_products,
    }
    return render(request, 'product_detail.html', context)