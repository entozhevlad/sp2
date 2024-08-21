from django.contrib import admin
from .models import Color, ProductCategory, Product, ProductVariant

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'material', 'volume')
    search_fields = ('name', 'category__name', 'material', 'volume')
    list_filter = ('category', 'material')
    ordering = ('name',)

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'color', 'main_image')
    search_fields = ('product__name', 'name', 'color__name')
    list_filter = ('product', 'color')

    def color_name(self, obj):
        return obj.color.name if obj.color else None
    color_name.short_description = 'Цвет'

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Сувенир'

