from django.db import models
from tinymce.models import HTMLField


class Excursion(models.Model):

    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание')
    long_description = HTMLField('Полное описание', null=True, blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
    title_place = models.CharField('Имя для карты', max_length=50)
    
    def __str__(self):
        return self.title


class Image(models.Model):

    excursion = models.ForeignKey('Excursion', on_delete=models.CASCADE)
    order = models.PositiveIntegerField('Порядок показа', db_index=True, default=0)
    image = models.ImageField('Изображение')
    
    def __str__(self):
        return f'{self.order} {self.excursion.title}'

    class Meta():
        ordering = ['order']