# Generated by Django 3.2.16 on 2023-01-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='title_place',
            field=models.CharField(default='test', max_length=50, verbose_name='Имя для карты'),
            preserve_default=False,
        ),
    ]