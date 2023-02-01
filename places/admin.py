from django.contrib import admin
from django.utils.html import format_html

from .models import Excursion, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']
    fields = ('image', 'preview_image', 'order',)

    def preview_image(self, obj):
        print(obj)
        small_width = obj.image.width / (obj.image.height / 150)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=small_width,
            height='150px',
            )
        )


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']
    fields = ('image', 'preview_image', 'order',)

    def preview_image(self, obj):
        print(obj)
        small_width = obj.image.width / (obj.image.height / 150)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=small_width,
            height='150px',
            )
        )
