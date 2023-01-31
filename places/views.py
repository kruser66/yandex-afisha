
from django.shortcuts import render
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
                'detailsUrl': '.'
            }
        }
        geo_places['features'].append(geo_point)

    context = {
        'geo_places': geo_places
    }

    return render(request, 'index.html', context)
