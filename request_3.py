from Authorization import authorization_r
from couriers_requests import get_couriers
from log_out import Print

'''
Тест-кейс №3. Проверка получения 5 курьеров с именем Максим
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить поисковый запрос на поиск курьера с параметром Максим- 
    система вернула код успеха 200
3) Сравнить количество курьеров с таким параметром - 
    их 5
4) Сравнить их имена с Максим - 
    у каждого курьера имя Максим
'''

def request_3():
    Print('Request 3')

    token = authorization_r()

    if token == -1:
        Print('Request 3 failed')
        return -1

    r = get_couriers(token, 1, 5, 0, 'Максим')

    if r == -1:
        Print('Request 3 failed')
        return -1

    if r['result']['count'] != 5:
        Print('Didnt find 5 couriers who named Maxim')
        Print('Request 3 failed')
        return -1

    Print('Find 5 couriers who named Maxim')
    couriers_list = r['result']['items']

    for courier in couriers_list:
        if courier['firstName'] != 'Максим':
            Print('Courier is not Maxim')
            Print('Request 3 failed')
            return -1

    Print('Every courier is Maxim ')
    Print('Success')
    return 'Success'

if __name__ == "__main__":
    request_3()