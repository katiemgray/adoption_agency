import requests
from secrets import PETS_RANDOM_URL


def random_pet():
    response = requests.get(PETS_RANDOM_URL)
    json_response = response.json()

    name = json_response['petfinder']['pet']['name']['$t']
    age = json_response['petfinder']['pet']['age']['$t']
    try:
        photo_url = json_response['petfinder']['pet']['media']['photos'][
            'photo'][2]['$t']
    except KeyError:
        photo_url = 'https://vignette.wikia.nocookie.net/warriorcatsclanroleplay/images/f/fc/Placeholder-pet.png/revision/latest?cb=20130716185616'

    return {"name": name, "age": age, "photo_url": photo_url}
