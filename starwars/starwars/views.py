from os import X_OK
import swapi
from swapi.settings import PLANETS


def update_data():
    planets = swapi.get_all(PLANETS)
    for planet in planets:
        print(planet)


update_data()
