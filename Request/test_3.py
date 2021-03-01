from request_authorisation import authorisation
import pytest

'''
Тест-кейс №3. Вход несуществующего пользователя в систему
1) Ввести неправильный логин и пароль - 
    бот не зашёл в систему
'''

def test_3():
    r = authorisation(wrong = True)

    assert r.status_code != 200, 'Логин и пароль оказались верны'