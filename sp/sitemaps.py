from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import ProductCategory, ProductVariant
from main.models import NewsImage,WorkExample, Service, Category
from contacts.models import Adress

class HomepageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['main:home', 'main:price']  # Возвращаем имена URL-адресов

    def location(self, item):
        return reverse(item)  # Возвращаем URL для каждого имени

class ProductVariantSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ProductVariant.objects.all()

class ProductCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return ProductCategory.objects.all()



class AddressSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return ['contacts:contacts']  # Вернем только один элемент - название URL для страницы контактов

    def location(self, item):
        return reverse(item)  # Вернем URL для указанного элемента