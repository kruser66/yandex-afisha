from django.db import models


class Excursion(models.Model):

    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание')
    long_description = models.TextField('Полное описание', null=True, blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
    
    def __str__(self):
        return self.title