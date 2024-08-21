from django.db import models

class Adress(models.Model):
    adress = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    graphic_1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='График ПН-ПТ')
    graphic_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='График СБ-ВС')
    class Meta:
        verbose_name = 'Адрес офиса'
        verbose_name_plural = 'Адреса офисов'