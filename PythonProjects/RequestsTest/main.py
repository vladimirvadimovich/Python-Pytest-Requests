import requests

URL = 'https://api.pokemonbattle.ru/v2/pokemons'
URL2 = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
TOKEN = '1c6eaa48ba3c748da730321721dd0c57'
HEADER = {
    'Content-type': 'application/json', 
    'trainer_token': TOKEN
    }
body_pokemons = {
    "name": "DonaldTrump",
    "photo_id": 22
}   

body_put_pokemons = {
    "pokemon_id": "135039",
    "name": "New Name",
    "photo_id": 22
}

body_add_pokeballs = {
    "pokemon_id": "135039"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)'''

'''response_create = requests.post(url = URL, headers = HEADER, json = body_pokemons)
print(response_create.text)'''

'''pokemon_id = response_create.text['id']
print(pokemon_id)'''

'''response_put = requests.put(url = URL, headers = HEADER, json = body_put_pokemons)
print(response_put.text)'''

response_add_pokeball = requests.post(url = URL2, headers = HEADER, json = body_add_pokeballs)
print(response_add_pokeball.text)
