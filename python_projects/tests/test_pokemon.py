import requests
import pytest

url = "https://api.pokemonbattle.ru/v2"
token = "e894f11937494259375f1a1a7524dc21"
header = {"Content-Type": "application/json", "trainer_token": token}


def test_trainer_response_code():
    response = requests.get(url=f"{url}/trainers?trainer_id=18993", headers=header)
    assert response.status_code == 200


def test_trainer_name():
    url = "https://api.pokemonbattle.ru/v2"
    trainer_id = 18993
    header = {"Content-Type": "application/json"}
    
    response = requests.get(f"{url}/trainers?trainer_id={trainer_id}", headers=header)
    
    # Ожидаемое имя тренера
    expected_name = "Динар13"
    
    # Получаем первый элемент из списка data, так как именно там хранится информация о тренере
    trainer_data = response.json()['data'][0]
    
    # Проверяем, что имя тренера совпадает с ожидаемым значением
    assert expected_name == trainer_data['trainer_name']
