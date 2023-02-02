from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase

from .models import Excursion, Image


class ImageInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = ['preview_image']
    list_display = ('image', 'preview_image', 'order',)
    ordering = ['order']

    def preview_image(self, obj):
        small_width = obj.image.width / (obj.image.height / 150)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=small_width,
            height='150px',
            )
        )


@admin.register(Excursion)
class ExcursionAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']
    list_display = ('image', 'preview_image', 'order',)
    ordering = ['order']

    def preview_image(self, obj):
        small_width = obj.image.width / (obj.image.height / 150)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=small_width,
            height='150px',
            )
        )
