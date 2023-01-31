from django.contrib import admin
from .models import Excursion, Image


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
