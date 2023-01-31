from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse
from .models import Excursion

def index(request):

    geo_places = {
        'type': 'FeatureCollection',
        'features': []
    }

    places = Excursion.objects.all()

    for place in places:
        geo_point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title_place,
                'placeId': place.pk,
                'detailsUrl': reverse('place_detail', kwargs={'place_id': place.pk})
            }
        }
        geo_places['features'].append(geo_point)

    context = {
        'geo_places': geo_places
    }

    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place_id = int(place_id)

    place = get_object_or_404(Excursion, pk=place_id)
    images = place.image_set.all().order_by('order')

    detail = {
        'title': place.title,
        'imgs': [img.image.url for img in images],
        'description_short': place.short_description ,
        'description_long': place.long_description,
        'coordinates': {
            'lng': str(place.longitude),
            'lat': str(place.latitude)
        }
    }

    return JsonResponse(detail, json_dumps_params={'indent': 4, 'ensure_ascii': False})