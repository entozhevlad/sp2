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

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
