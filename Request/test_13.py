from request_authorisation import authorisation
from event_79 import included_in_consolidation
import Pathes
import pytest

'''
Тест-кейс №13. Создание блока событий 79
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на создание блока событий с точкой назначения "1202" - 
    Блок был создан
'''


def test_13():
    token = authorisation()

    destinationPointId = Pathes.destinationPointId_1202

    r = included_in_consolidation(token, destinationPointId)

    destinationPoint = r['result']['destinationPoint']

    assert destinationPoint['code'] == '1202', 'Попал в другой блок'
