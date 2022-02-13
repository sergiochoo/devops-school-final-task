from django.core import serializers
from django.http import JsonResponse

from .models import Planet, Character
from .swapi import get_all_planets, get_all_characters


def clear_data(request):
    characters_deleted, _ = Character.objects.all().delete()
    planets_deleted, _ = Planet.objects.all().delete()
    return JsonResponse({
        "status": "success",
        "characters_deleted": characters_deleted,
        "planets_deleted": planets_deleted,
    })


def sync_data(request):
    planets_created = 0
    characters_created = 0
    for planet in get_all_planets():
        _, created = Planet.objects.update_or_create(
            url=planet["url"],
            name=planet["name"],
            gravity=planet["gravity"],
            climate=planet["climate"],
        )
        if created:
            planets_created += 1
    for character in get_all_characters():
        _, created = Character.objects.update_or_create(
            url=character["url"],
            name=character["name"],
            gender=character["gender"],
            homeworld=Planet.objects.get(url=character["homeworld"]),
        )
        if created:
            characters_created += 1
    return JsonResponse({
        "status": "success",
        "planets_created": planets_created,
        "characters_created": characters_created,
    })


def get_report(request):
    planets = [planet.get_json() for planet in Planet.objects.all()]
    return JsonResponse({"status": "success", "planets": planets})
