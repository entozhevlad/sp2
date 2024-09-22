from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.utils.text import slugify
from django.urls import reverse

class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название цвета')
    image = models.ImageField(upload_to='color_images/', blank=True, null=True, verbose_name='Изображение цвета')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Color.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                old_instance.image.delete(False)
        super().save(*args, **kwargs)

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

    def get_absolute_url(self):
        return reverse('catalog:catalog_by_category', kwargs={'category_slug': self.slug})

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    material = models.CharField(max_length=255, blank=True, null=True, verbose_name='Материал')
    appointment = models.CharField(blank=True, null=True, verbose_name='Назначение')
    kit = models.CharField(blank=True, null=True, verbose_name='Комплектация')
    additional_details = models.TextField(blank=True, null=True, verbose_name='Дополнительные детали')
    optional_image = models.ImageField(upload_to='product_images/', blank=True, null=True,
                                           verbose_name='Опциональное изображение (Размерная сетка)')
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

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Product.objects.get(pk=self.pk)
            if old_instance.optional_image and old_instance.optional_image != self.optional_image:
                old_instance.optional_image.delete(False)
        super().save(*args, **kwargs)

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

    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='Slug', null=True)

    class Meta:
        verbose_name = 'Вариант сувенира'
        verbose_name_plural = 'Варианты сувенира'

    def __str__(self):
        return f"{self.product.name} - {self.color.name if self.color else 'Без цвета'}"

    def get_other_variants(self):
        return self.product.variants.exclude(id=self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = f"{self.product.name} {self.color.name if self.color else ''}"
            self.slug = slugify(base_slug)
            unique_slug = self.slug
            num = 1
            while ProductVariant.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug

        if self.pk:
            old_instance = ProductVariant.objects.get(pk=self.pk)
            if old_instance.main_image and old_instance.main_image != self.main_image:
                old_instance.main_image.delete(False)
            if old_instance.additional_image_1 and old_instance.additional_image_1 != self.additional_image_1:
                old_instance.additional_image_1.delete(False)
            if old_instance.additional_image_2 and old_instance.additional_image_2 != self.additional_image_2:
                old_instance.additional_image_2.delete(False)
            if old_instance.additional_image_3 and old_instance.additional_image_3 != self.additional_image_3:
                old_instance.additional_image_3.delete(False)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})

@receiver(post_delete, sender=Color)
def delete_color_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

@receiver(post_delete, sender=Product)
def delete_product_image_on_delete(sender, instance, **kwargs):
    if instance.optional_image:
        instance.optional_image.delete(False)

@receiver(post_delete, sender=ProductVariant)
def delete_variant_images_on_delete(sender, instance, **kwargs):
    if instance.main_image:
        instance.main_image.delete(False)
    if instance.additional_image_1:
        instance.additional_image_1.delete(False)
    if instance.additional_image_2:
        instance.additional_image_2.delete(False)
    if instance.additional_image_3:
        instance.additional_image_3.delete(False)
