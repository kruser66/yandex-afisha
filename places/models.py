from django.db import models
from tinymce.models import HTMLField


class Excursion(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение')
    order = models.PositiveIntegerField('Порядок показа', db_index=True, default=0)
    excursion = models.ForeignKey('Excursion', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order} {self.excursion.title}'

    class Meta():
        ordering = ['order']
