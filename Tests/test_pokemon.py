import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/pokemons'
URL2 = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
URL3 = 'https://api.pokemonbattle.ru/v2/trainers'
TOKEN = '1c6eaa48ba3c748da730321721dd0c57'
HEADER = {
    'Content-type': 'application/json', 
    'trainer_token': TOKEN
    }
TRAINER_ID = 11262

def test_status_code(): 
    response =  requests.get(url = URL3, params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_of_response():
    response_get_trainer = requests.get(url = URL3, params = {'trainer_id' : TRAINER_ID})
    assert response_get_trainer.json()["data"][0]["trainer_name"] == "Garry Potter from Hogwarts"