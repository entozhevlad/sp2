from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Service, NewsImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_editable = ['category']


from django.utils.safestring import mark_safe



@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = (
    'title', 'created_at', 'get_image_thumbnail', 'get_image_big_thumbnail', 'get_image_mobile_thumbnail')
    readonly_fields = ('created_at', 'get_image_thumbnail', 'get_image_big_thumbnail', 'get_image_mobile_thumbnail')

    # Организация полей на странице изменения
    fieldsets = (
        (None, {
            'fields': ('title', 'created_at')
        }),
        ('Изображения', {
            'fields': (
                ('image', 'get_image_thumbnail'),  # Обычное изображение и его миниатюра
                ('image_big', 'get_image_big_thumbnail'),  # Большое изображение и его миниатюра
                ('image_mobile', 'get_image_mobile_thumbnail')  # Мобильное изображение и его миниатюра
            )
        }),
    )

    # Метод для отображения миниатюры обычного изображения
    def get_image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' height='50px'>")
        return "Нет изображения"

    get_image_thumbnail.short_description = 'Миниатюра'

    # Метод для отображения миниатюры большого изображения
    def get_image_big_thumbnail(self, obj):
        if obj.image_big:
            return mark_safe(f"<img src='{obj.image_big.url}' height='50px'>")
        return "Нет изображения"

    get_image_big_thumbnail.short_description = 'Миниатюра большого изображения'

    # Метод для отображения миниатюры мобильного изображения
    def get_image_mobile_thumbnail(self, obj):
        if obj.image_mobile:
            return mark_safe(f"<img src='{obj.image_mobile.url}' height='50px'>")
        return "Нет изображения"

    get_image_mobile_thumbnail.short_description = 'Миниатюра мобильного изображения'


admin.site.site_header = 'Админ-панель Студия Печати'
admin.site.site_title = 'Админ-панель Студия Печати'