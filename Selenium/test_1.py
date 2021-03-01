from login_page import login
from login_page import check_enty
import time
import pytest

'''
Тест-кейс №1. Вход существующего пользователя в систему
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
'''

def test_s_1():
    driver = login()

    time.sleep(0.5)

    check_enty(driver)

    driver.close()
if __name__ == "__main__":
    test_s_1()