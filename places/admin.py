from django.contrib import admin
from .models import Excursion, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'order')

@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
