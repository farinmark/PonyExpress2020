from request_authorisation import authorisation
from geography import get_by_id

'''
Тест-кейс №16 Тестирование отрицательной работы сервиса географии
1) Войти на сайт -
    Получение токена авторизации
2) Отправить запрос на сервис на поиск адреса объекта по неправильному id -
    Система не вернула ошибку "Object not found"
'''

def test_16():
    token = authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'

    r = get_by_id(token, id_)

    assert r['metadata']['message'] == 'Object not found', 'Система не вернула ошибку Object not found'