from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CategoryForm, ServiceForm, ColorForm, ProductCategoryForm, ProductForm, ProductVariantForm, AdressForm
from main.models import Category, Service
from catalog.models import Color, ProductCategory, Product, ProductVariant
from contacts.models import Adress

@login_required
def admin_sp(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    colors = Color.objects.all()
    product_categories = ProductCategory.objects.all()
    products = Product.objects.all()
    product_variants = ProductVariant.objects.all()
    adresses = Adress.objects.all()

    context = {
        'categories': categories,
        'services': services,
        'colors': colors,
        'product_categories': product_categories,
        'products': products,
        'product_variants': product_variants,
        'adresses': adresses,
    }

    return render(request, 'admin_sp.html', context)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': category, 'type': 'category'})

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})

@login_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'edit_service.html', {'form': form})

@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': service, 'type': 'service'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_sp')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def edit_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ColorForm(instance=color)
    return render(request, 'edit_color.html', {'form': form})

@login_required
def delete_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        color.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': color, 'type': 'color'})

# ProductCategory Views
@login_required
def add_product_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductCategoryForm()
    return render(request, 'add_edit_product_category.html', {'form': form})

@login_required
def edit_product_category(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductCategoryForm(instance=category)
    return render(request, 'add_edit_product_category.html', {'form': form})

@login_required
def delete_product_category(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': category, 'type': 'product_category'})

# Product Views
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductForm()
    return render(request, 'add_edit_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': product, 'type': 'product'})

# ProductVariant Views
@login_required
def add_product_variant(request):
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductVariantForm()
    return render(request, 'add_edit_product_variant.html', {'form': form})

@login_required
def edit_product_variant(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, request.FILES, instance=variant)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ProductVariantForm(instance=variant)
    return render(request, 'add_edit_product_variant.html', {'form': form})

@login_required
def delete_product_variant(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)
    if request.method == 'POST':
        variant.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': variant, 'type': 'product_variant'})

# Adress Views
@login_required
def add_adress(request):
    if request.method == 'POST':
        form = AdressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = AdressForm()
    return render(request, 'add_edit_address.html', {'form': form})

@login_required
def edit_adress(request, adress_id):
    adress = get_object_or_404(Adress, id=adress_id)
    if request.method == 'POST':
        form = AdressForm(request.POST, instance=adress)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = AdressForm(instance=adress)
    return render(request, 'add_edit_address.html', {'form': form})

@login_required
def delete_adress(request, adress_id):
    adress = get_object_or_404(Adress, id=adress_id)
    if request.method == 'POST':
        adress.delete()
        return redirect('admin_sp')
    return render(request, 'confirm_delete.html', {'object': adress, 'type': 'adress'})

@login_required
def add_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ColorForm()
    return render(request, 'add_edit_color.html', {'form': form})

@login_required
def edit_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            form.save()
            return redirect('admin_sp')
    else:
        form = ColorForm(instance=color)
    return render(request, 'add_edit_color.html', {'form': form})