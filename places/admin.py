from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase
from .models import Excursion, Image


def format_preview_image(image, height='200px'):
    return format_html('<img src="{url}" height="{height}"/>',
                       url=image.image.url,
                       height=height,
                       )


class ImageInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = ['preview_image']
    list_display = ('image', 'preview_image', 'order',)
    ordering = ['order']

    def preview_image(self, image):
        return format_preview_image(image)


@admin.register(Excursion)
class ExcursionAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']
    list_display = ['excursion', 'preview_image', 'image']
    list_filter = ['excursion']

    def preview_image(self, image):
        return format_preview_image(image)
