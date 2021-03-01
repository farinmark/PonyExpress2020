from login_page import login
from login_page import check_enty
from service_menu import editing_user_groups_button
import time
import pytest

'''
Тест-кейс №5. Просмотр списка групп пользователей
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» -
    В выпавшем списке доступен пункт «Сервис» - «Управление» разрешениями»
4) Выбрать пункт «Группы пользователей» - 
    Открылась форма «Редактирование групп пользователей»
'''

def test_s_5():
    driver = login()

    time.sleep(0.5)

    check_enty(driver)

    time.sleep(0.5)

    editing_user_groups_button(driver)

    driver.close()

if __name__ == "__main__":
    test_s_5()