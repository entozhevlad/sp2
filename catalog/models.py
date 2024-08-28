from django.db import models
from django.utils.text import slugify

class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название цвета')
    image = models.ImageField(upload_to='color_images/', blank=True, null=True, verbose_name='Изображение цвета')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

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
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    material = models.CharField(max_length=255, blank=True, null=True, verbose_name='Материал')
    appointment = models.TextField(blank=True, null=True, verbose_name='Назначение')
    kit = models.TextField(blank=True, null=True, verbose_name='Комплектация')
    additional_details = models.TextField(blank=True, null=True, verbose_name='Дополнительные детали')
    # Дополнительные свойства
    height = models.CharField(max_length=255, blank=True, null=True, verbose_name='Высота')
    size = models.CharField(max_length=255, blank=True, null=True, verbose_name='Размер')
    density = models.CharField(max_length=255, blank=True, null=True, verbose_name='Плотность')
    diameter = models.CharField(max_length=255, blank=True, null=True, verbose_name='Диаметр')
    application_method = models.CharField(max_length=255, blank=True, null=True, verbose_name='Способ нанесения')
    volume = models.CharField(max_length=255, blank=True, null=True, verbose_name='Объём')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сувенир'
        verbose_name_plural = 'Сувениры'

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', verbose_name='Сувенир')
    name = models.CharField(max_length=255, verbose_name='Название', default=product.name)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, related_name='variants', verbose_name='Цвет')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True, default=0.00)
    main_image = models.ImageField(upload_to='variant_images/', blank=True, null=True,
                                   verbose_name='Главное изображение')
    additional_image_1 = models.ImageField(upload_to='variant_images/', blank=True, null=True,
                                           verbose_name='Дополнительное изображение 1')
    additional_image_2 = models.ImageField(upload_to='variant_images/', blank=True, null=True,
                                           verbose_name='Дополнительное изображение 2')
    additional_image_3 = models.ImageField(upload_to='variant_images/', blank=True, null=True,
                                           verbose_name='Дополнительное изображение 3')

    class Meta:
        verbose_name = 'Вариант сувенира'
        verbose_name_plural = 'Варианты сувенира'

    def __str__(self):
        return f"{self.product.name} - {self.color.name if self.color else 'Без цвета'}"

    def get_other_variants(self):
        return self.product.variants.exclude(id=self.id)


