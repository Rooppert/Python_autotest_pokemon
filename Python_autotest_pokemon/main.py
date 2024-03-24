import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '51254d80e9c8d6c4f37e247a2b0c5d4f'
TRANIER_ID = '158'
HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}


body_pokemon = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_pokemon) #создаем покемона

print(response.text)



POKEMON_ID = response.json()['id'] # создаем переменную и помещаем в нее ID из ответа



new_body_pokemon = {
    "pokemon_id": POKEMON_ID,
    "name": "Pokemon",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = new_body_pokemon) #переименовываем покемона

print(response_name.text)



body_pokebol = {
    "pokemon_id": POKEMON_ID
}

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokebol) #ловим покемона

print(response_pokebol.text)