import requests

URL = 'https://api.pokemonbattle.ru'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : 'f5c4f324fe4ba09b7c93ec73ad63a9e3'}
body_create = {
    "name": "БиБоБо",
    "photo_id": 12
}
body_change = {
    "pokemon_id": "324850",
    "name": "Ёклмн",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "324850"
}

'''response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response.text)'''


'''response_to_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change)
print(response_to_change.text)'''

response_catch = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
