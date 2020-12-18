from  Authorization import authorization_r
from log_out import Print
from couriers_requests import get_courier_by_id

'''
Тест-кейс №2. Проверка получения конфигурации бэкэнда
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить запрос на получение курьера по id - 
    система вернула код успеха 200
3) Сравнить имя и фамилию курьера - 
    имя и фамилия курьера совпадают с ожидаемыми
'''

def request_2():
    Print('request 2')

    token = authorization_r()

    if token == -1:
        return -1

    r = get_courier_by_id(token, '359afb0c-b870-4610-9233-524db1d5a029')

    if r == -1:
        return -1
    r = r['result']

    if r['firstName'] != 'Евгений ' or r['lastName'] != '(СТД) Бурлаченко':
        Print('Wrong courier')
        return -1
    else:
        Print('Right courier')
        Print('Success')
        return 'Success'


if __name__ == "__main__":
    request_2()