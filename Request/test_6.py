from request_authorisation import authorisation
from user_groups_requests import get_all_groups
from user_groups_requests import create_group
from user_groups_requests import delete_group
import datetime
import pytest

'''
Тест-кейс №6. Проверка права на создание группы пользователей и удаление её
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
3) Отправить запрос на создание группы - 
    система вернула код успеха 200
4) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
5) Искать среди групп пользователей новую созданную группу - 
    группа нашлась
6) Отправить запрос на удаление созданной группы - 
    система вернула код успеха 200
7) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
8) Искать среди групп пользователей новую созданную группу - 
    группа не нашлась
'''

def test_6():
    token = authorisation()

    r = get_all_groups(token)

    assert r['result'] != None, 'Не смог найти группы'

    date = datetime.datetime.now()
    name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop_request')

    for group in r['result']:
        assert group['displayName'] != name, 'Группа с именем: ' + name + ' уже существует'

    r = create_group(token, name)

    assert r['result'] != None, 'Не смог создать группу'

    id_ = r['result']['id']

    r = get_all_groups(token)

    assert r['result'] != None, 'Не смог найти группы'

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id_:
            exists = 1

    assert exists, 'Не нашёл созданную группу'

    delete_group(token, id_)

    r = get_all_groups(token)

    assert r['result'] != None, 'Не смог найти группы'

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id_:
            exists = 1

    assert not exists, 'Группа не удалилась'