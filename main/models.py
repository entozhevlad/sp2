from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from PIL import Image
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    is_visible = models.BooleanField(default=True, verbose_name='Отображается на сайте')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name



class NewsImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/')
    image_big = models.ImageField(upload_to='news/big/', blank=True, null=True)
    image_mobile = models.ImageField(upload_to='news/mobile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = NewsImage.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                old_instance.image.delete(False)
            if old_instance.image_big and old_instance.image_big != self.image_big:
                old_instance.image_big.delete(False)
            if old_instance.image_mobile and old_instance.image_mobile != self.image_mobile:
                old_instance.image_mobile.delete(False)
        super().save(*args, **kwargs)

class WorkExample(models.Model):
    title = models.CharField(max_length=12)
    image = models.ImageField(upload_to='work_examples/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры работ'

    def __str__(self):
        return self.title

    def clean(self):
        img = Image.open(self.image)

        width, height = img.size

        if width != height:
            raise ValidationError('Изображение должно быть квадратным.')

    def save(self, *args, **kwargs):
        if WorkExample.objects.count() >= 10:
            raise ValidationError('Достигнуто максимальное количество примеров работ (10).')

        self.full_clean()
        super().save(*args, **kwargs)

@receiver(post_delete, sender=NewsImage)
def delete_news_images_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
    if instance.image_big:
        instance.image_big.delete(False)
    if instance.image_mobile:
        instance.image_mobile.delete(False)

@receiver(post_delete, sender=WorkExample)
def delete_work_example_images_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)