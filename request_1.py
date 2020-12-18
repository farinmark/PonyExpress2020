import  Authorization
from log_out import Print
from get_request import get_request


'''
Тест-кейс №1. Проверка получения конфигурации бэкэнда
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить запрос на получение конфигурации бэкэнда - 
    система вернула код успеха 200
'''

def request_1():
    Print('request 1')
    token = Authorization.authorization_r()
    if token == -1:
        return -1
    Print('Request was sent')
    r = get_request(token, 0, '/api/v1/configurations/get-all')
    if r == -1 or r.status_code != 200:
        Print("request 1 failed")
        return -1
    Print('Success')
    return "Success"

if __name__ == "__main__":
    Print(request_1())