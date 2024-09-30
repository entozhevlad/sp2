from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = (
        'product', 'name', 'color', 'get_main_image_thumbnail',
        'get_additional_image_1_thumbnail', 'get_additional_image_2_thumbnail',
        'get_additional_image_3_thumbnail', 'slug'
    )
    search_fields = ('product__name', 'name', 'color__name', 'slug')
    list_filter = ('product', 'color')

    # Организуем поля на странице редактирования
    fieldsets = (
        (None, {
            'fields': ('product', 'name', 'color', 'price', 'slug')
        }),
        ('Изображения', {
            'fields': (
                ('main_image', 'get_main_image_thumbnail'),  # Главное изображение и миниатюра
                ('additional_image_1', 'get_additional_image_1_thumbnail'),  # Доп. изображение 1 и миниатюра
                ('additional_image_2', 'get_additional_image_2_thumbnail'),  # Доп. изображение 2 и миниатюра
                ('additional_image_3', 'get_additional_image_3_thumbnail')  # Доп. изображение 3 и миниатюра
            )
        }),
    )

    readonly_fields = (
        'get_main_image_thumbnail', 'get_additional_image_1_thumbnail',
        'get_additional_image_2_thumbnail', 'get_additional_image_3_thumbnail'
    )

    prepopulated_fields = {'slug': ('name',)}  # Заполнение slug на основе другого поля

    # Отображение миниатюры главного изображения
    def get_main_image_thumbnail(self, obj):
        if obj.main_image:
            return mark_safe(f"<img src='{obj.main_image.url}' width='50px'>")
        return "Нет изображения"

    get_main_image_thumbnail.short_description = 'Главное изображение'

    # Отображение миниатюры дополнительного изображения 1
    def get_additional_image_1_thumbnail(self, obj):
        if obj.additional_image_1:
            return mark_safe(f"<img src='{obj.additional_image_1.url}' width='50px'>")
        return "Нет изображения"

    get_additional_image_1_thumbnail.short_description = 'Доп. изображение 1'

    # Отображение миниатюры дополнительного изображения 2
    def get_additional_image_2_thumbnail(self, obj):
        if obj.additional_image_2:
            return mark_safe(f"<img src='{obj.additional_image_2.url}' width='50px'>")
        return "Нет изображения"

    get_additional_image_2_thumbnail.short_description = 'Доп. изображение 2'

    # Отображение миниатюры дополнительного изображения 3
    def get_additional_image_3_thumbnail(self, obj):
        if obj.additional_image_3:
            return mark_safe(f"<img src='{obj.additional_image_3.url}' width='50px'>")
        return "Нет изображения"

    get_additional_image_3_thumbnail.short_description = 'Доп. изображение 3'
