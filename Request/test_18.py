from request_authorisation import authorisation
from geography import get_polygon_with_coordinates_by_address_id

'''
Тест-кейс №18 Тестирование отрицательной работы сервиса географии
1) Войти в систему -
    Получение токена на авторизацию
2) Отправить запрос на получение координат полигона по неправильному id -
    Система не вернула ошибку $_ADDRESS_NOT_FOUND_$
'''

def test_18():
    token = authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'
    number = '11-1111-1111'

    r = get_polygon_with_coordinates_by_address_id(token, id_, number)

    assert '$_ADDRESS_NOT_FOUND_$' in r['metadata']['message'], 'Система не вернула ошибку $_ADDRESS_NOT_FOUND_$'