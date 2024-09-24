from django.contrib.sitemaps import Sitemap
from catalog.models import ProductCategory, ProductVariant


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

