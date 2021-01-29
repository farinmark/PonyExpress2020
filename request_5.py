from Authorization import authorization_r
from log_out import Print
from user_group_requests import create_group
from user_group_requests import delete_group
from user_group_requests import get_all_groups
import datetime

'''
Тест-кейс №5. Проверка права на создание группы пользователей и удаление её
1) Войти в систему - 
    бот зашёл в систуме
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

def request_5():
    Print('Request 5')

    token = authorization_r()

    if token == -1:
        Print('Request 5 failed')
        return -1

    r = get_all_groups(token)

    if r == -1:
        Print('Request 5 failed')
        return -1

    if r['result'] == None:
        Print('Cant find groups')
        Print('Request 5 failed')
        return -1

    Print('Get all groups of users')

    date = datetime.datetime.now()
    name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop_request')

    for group in r['result']:
        if group['displayName'] == name:
            Print('Group with name: ' + name + 'already exist')
            Print('Request 5 failed')
            return -1

    r = create_group(token, name)

    if r['result'] == None:
        Print('Cant create group')
        Print('Request 5 failed')
        return -1

    id = r['result']['id']

    r = get_all_groups(token)

    if r == -1:
        Print('Request 5 failed')
        return -1

    if r['result'] == None:
        Print('Cant find groups')
        Print('Request 5 failed')
        return -1

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id:
            exists = 1

    if not exists:
        Print('Cant find created group')
        Print('Request 5 failed')
        return -1

    Print('Found created group with name: ' + name + ' и id: ' + id)

    r = delete_group(token, id)

    if r == -1:
        Print('Request 5 failed')
        return -1

    r = get_all_groups(token)

    if r == -1:
        Print('Request 5 failed')
        return -1

    if r['result'] == None:
        Print('Cant find group')
        Print('Request 5 failed')
        return -1

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id:
            exists = 1

    if exists:
        Print('Group wasn\'t deleted')
        Print('Request 5 failed')
        return -1

    Print('Group was deleted')

    Print('Success')
    return 'Success'

if __name__ == "__main__":
    request_5()