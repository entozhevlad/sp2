from django.db import models

# Create your models here.
from django.utils.text import slugify

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Добавьте это поле

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Название')
    description = models.TextField()
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name='Цвет')
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,verbose_name='Высота')
    diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Диаметр')
    material = models.CharField(max_length=255, blank=True, null=True, verbose_name='Material')
    application_method = models.CharField(max_length=255, blank=True, null=True, verbose_name='Метод нанесения')
    volume = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Объём')
    additional_details = models.TextField(blank=True, null=True, verbose_name='Дополнительные детали')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True,
                              verbose_name='Фото')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cувенир'
        verbose_name_plural = 'Сувениры'

    def __str__(self):
        return self.name