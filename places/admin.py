from django.contrib import admin
from .models import Excursion


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass

