from request_authorisation import authorisation
from geography import get_by_id
'''
Тест-кейс №16 Тестирование правильной работы сервиса географии
1) Войти на сайт -
    Получение токена авторизации
2) Отправить запрос на сервис на поиск адреса объекта по неправильному id -
    Система нашла объект
'''


def test_19():
    token = authorisation()

    id_ = 'ad9204fb-4007-4185-9288-503e55f66f0c'

    r = get_by_id(token, id_)

    assert r['result'] is not None, 'Система не нашла объект'