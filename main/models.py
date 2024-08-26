from django.db import models
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

