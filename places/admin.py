from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase
from .models import Excursion, Image


def format_preview_image(image, height='200px'):
    return format_html(
        '<img src="{url}" height="{height}"/>',
        url=image.image.url,
        height=height,
    )


class ImageStackedInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = [format_preview_image]
    list_display = ('image', format_preview_image, 'order',)
    ordering = ['order']


@admin.register(Excursion)
class ExcursionAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageStackedInline
    ]
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [format_preview_image]
    list_display = ['excursion', format_preview_image, 'image']
    list_filter = ['excursion']

