from Authorization import authorization_r
from log_out import Print
from warehouse_requests import get_condition_parameters
from condition_parametrs import codes as right_codes

'''
Тест-кейс №4. Проверка получения всех параметров состояний у склада
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить поисковый запрос на получение всех параметров состояний - 
    система вернула код успеха 200
3) Сравнить их количество с ожидаемым - 
    они совпадают
4) Сравнить параметры состояний с ожидаемыми - 
    они не отличаются
'''

def request_4():
    Print('Request 4')

    token = authorization_r()

    if token == -1:
        Print('Request 4 failed')
        return -1

    r = get_condition_parameters(token)

    if r == -1:
        Print('Request 4 failed')
        return -1

    code_list = r['result']

    now_codes = []

    for code in code_list:
        now_codes.append([code['code'], code['name']])

    if len(now_codes) != len(right_codes):
        Print('Number of condition params diff of expected')
        Print('Request 4 failed')
        return -1

    Print('Number of condition params didnt diff of expected')

    for code in now_codes:
        if not code in right_codes:
            Print('Condition params diff of expected')
            Print('Request 4 failed')
            return -1

    Print('Condition params didnt diff of expected')

    Print('Success')
    return 'Success'

if __name__ == "__main__":
    request_4()