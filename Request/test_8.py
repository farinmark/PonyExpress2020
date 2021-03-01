from request_authorisation import authorisation
from event_71 import without_sorting_and_couriers
import pytest

'''
Тест-кейс №8. Создание блока событий 71 без курьера
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на создание блока событий 71 без курьера -
    Блок был создан
'''

def test_8():
    token = authorisation()

    r = without_sorting_and_couriers(token)

    assert r['result']['id'] != None, 'Блок не был создан'
