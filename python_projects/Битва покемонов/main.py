import requests

url = "https://api.pokemonbattle.ru/v2"
token = "e894f11937494259375f1a1a7524dc21"
header = {
    "Content-Type": "application/json",
    "trainer_token": token
}
data1 = {
    "name": "generate",
    "photo_id": -1
}
response1 = requests.post(url = f "{url}/pokemons", headers = header, json = data1)
if response1.status_code == 201:
    pokemon_data = response1.json()
pokemon_id = pokemon_data.get("id")
data2 = {
    "pokemon_id": str(pokemon_id),
    "name": "generate",
    "photo_id": -1
}
response2 = requests.put(url = f "{url}/pokemons", headers = header, json = data2)
if response2.status_code == 200:
    pokemon_data_updated = response2.json()
pokemon_id_updated = pokemon_data_updated.get("id")
data3 = {
    "pokemon_id": str(pokemon_id_updated)
}
response3 = requests.post(url = f "{url}/trainers/add_pokeball", headers = header, json = data3)
print(response1.text)
print(response2.text)
print(response3.text)