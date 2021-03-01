from login_page import login
from login_page import check_enty
from main_page import quit
import time
import pytest

'''
Тест-кейс №2. Выход пользователя из системы
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку выход в верхнем правом углу окна системы - 
    Пользователь вышел из системы, открылась страница «Вход в систему»
'''

def test_s_2():
    driver = login()

    time.sleep(0.5)

    check_enty(driver)

    time.sleep(0.5)

    quit(driver)

    driver.close()

if __name__ == "__main__":
    test_s_2()