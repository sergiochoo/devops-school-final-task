import json
import logging
import urllib.request

logger = logging.getLogger(__name__)
BASE_API_URL = "https://swapi.dev/api"


def fetch_json_request(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return json.loads(data.decode("utf-8"))


def get_all_planets():
    next_page = f'{BASE_API_URL}/planets/'
    while next_page:
        planets_resp = fetch_json_request(next_page)
        next_page = planets_resp.get('next')
        for planet in planets_resp.get('results', []):
            logger.warning(f'planet: {planet["name"]}')
            yield planet


def get_all_characters():
    next_page = f'{BASE_API_URL}/people/'
    while next_page:
        planets_resp = fetch_json_request(next_page)
        next_page = planets_resp.get('next')
        for planet in planets_resp.get('results', []):
            logger.warning(f'planet: {planet["name"]}')
            yield planet
