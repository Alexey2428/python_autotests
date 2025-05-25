import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : 'f5c4f324fe4ba09b7c93ec73ad63a9e3'}
TRAINER_ID = '33579'
def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Алексей'