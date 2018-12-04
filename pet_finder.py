import requests
from secrets import PETS_RANDOM_URL


def random_pet():
    response = requests.get(PETS_RANDOM_URL)
    json_response = response.json()

    name = json_response['petfinder']['pet']['name']['$t']
    age = json_response['petfinder']['pet']['age']['$t']
    photo_url = json_response['petfinder']['pet']['media']['photos']['photo'][
        2]['$t']

    return {"name": name, "age": age, "photo_url": photo_url}
