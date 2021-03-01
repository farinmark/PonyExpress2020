from request_authorisation import authorisation
from event_79 import included_in_consolidation
from event_79 import add_object
import Pathes
import pytest

'''
Тест-кейс №14. Ввод несуществующего места в блок событий 79
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на создание блока событий с точкой назначения "1202" - 
    Блок был создан
3) Отправить запрос на добавление накладной с номером "99- 9999-9999/999" -
    Система вернула ошибку «Отсутствует введенное место накладной»
'''

def test_14():
    token = authorisation()

    destinationPointId = Pathes.destinationPointId_1202

    r = included_in_consolidation(token, destinationPointId)

    destinationPoint = r['result']['destinationPoint']

    assert destinationPoint['code'] == '1202', 'Попал в другой блок'

    id_ = r['result']['id']

    number = "99-9999-9999/999"

    r = add_object(token, id_, number)

    assert r['metadata']['message'] == "Отсутствует введенное место накладной", 'Система не вернула ошибку «Отсутствует введенное место накладной»'
