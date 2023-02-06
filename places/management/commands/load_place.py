import os
import json
import requests
from urllib.parse import unquote, urlsplit
from django.core.files.base import ContentFile
from places.models import Excursion, Image
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '''Загрузка локаций в базу данных по ссылке на JSON-данные.
    Примеры структуры данных и готовые ссылки можно посмотреть: https://github.com/devmanorg/where-to-go-places 
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            nargs='+',
            help='Ссылка на данные в JSON формате'
        )

    def handle(self, *args, **options):
        place_url = options['json_url'][0]
        response = requests.get(place_url)
        response.raise_for_status()
        try:
            place = response.json()
        except json.decoder.JSONDecodeError as err:
            print(f'Неверный формат данных. Ошибка: {err}')
            return

        try:
            new_excursion = Excursion.objects.create(
                title=place['title'],
                short_description=place['description_short'],
                long_description=place['description_long'],
                longitude=place['coordinates']['lng'],
                latitude=place['coordinates']['lat'],
            )
        except KeyError as err:
            print(f'Неверный формат данных. Ошибка: {err}')
            return

        for index, image_url in enumerate(place['imgs']):
            url = unquote(image_url)
            filename = os.path.split(urlsplit(url).path)[1]

            response = requests.get(url)
            response.raise_for_status()

            img = Image.objects.create(
                order=index,
                excursion=new_excursion,
            )
            img.save()
            img.image.save(filename, ContentFile(response.content), save=True)

        print(f'Экскурсия: {new_excursion} загружена')
