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
            'url',
            help='Ссылка на данные в JSON формате'
        )

    def handle(self, *args, **options):
        place_url = options['url']
        response = requests.get(place_url)
        response.raise_for_status()
        try:
            place = response.json()
        except json.decoder.JSONDecodeError as err:
            print(f'Неверный формат данных. Ошибка: {err}')
            return

        try:
            new_excursion, exc_created = Excursion.objects.get_or_create(
                title=place['title'],
                short_description=place.get('description_short') if place.get('description_short') else '',
                long_description=place.get('description_long') if place.get('description_long') else '',
                longitude=place['coordinates']['lng'],
                latitude=place['coordinates']['lat'],
            )
        except KeyError as err:
            print(f'Неверный формат данных. Ошибка: {err}')
            return

        if exc_created:
            if place.get('imgs'):
                for index, image_url in enumerate(place['imgs']):
                    url = unquote(image_url)
                    filename = os.path.split(urlsplit(url).path)[1]

                    response = requests.get(url)
                    response.raise_for_status()

                    Image.objects.get_or_create(
                        order=index,
                        excursion=new_excursion,
                        image= ContentFile(content=response.content, name=filename)
                    )
            print(f'Экскурсия: {new_excursion} загружена')
        else:
            print(f'Экскурсия: {new_excursion} была загружена ранее')
