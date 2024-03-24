import requests
import pytest
Host = "https://api.pokemonbattle.me/v2"
Trainer_ID = "158"
Trainer_token = "51254d80e9c8d6c4f37e247a2b0c5d4f"
HEADERS = {"Content-Type" :"application/json",
           "trainer_token" :Trainer_token  }

def test_status_code ():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : Trainer_ID})  # проверка статус кода
    assert response.status_code == 200 


Cases = [                                                                # параметры для проверок
    ("trainer_name", "rooppert"),    
    ("city", "Санкт-Петербург"),
    ("photo", "/images/trainer_avatar_01.png"),
    ("id", "158"),
    ("level", "2")
]                                                 


@pytest.mark.parametrize("key, value", Cases)


def test_parametrize_body(key, value):
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : Trainer_ID}) # проверка имени и города тренера
    assert response.json()["data"][0][key] == value
