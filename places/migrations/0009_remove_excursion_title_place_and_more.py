# Generated by Django 4.1.6 on 2023-02-06 06:04

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_excursion_long_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excursion',
            name='title_place',
        ),
        migrations.AlterField(
            model_name='excursion',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='image',
            name='excursion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.excursion'),
        ),
    ]