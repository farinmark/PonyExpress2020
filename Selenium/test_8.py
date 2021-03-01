from login_page import login
from login_page import check_enty
from arrived_at_the_warehouse_no_sorting import check_menu
import time
import pytest

'''
Тест-кейс №8. Создание блока событий 71 без курьера
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «71. Прибыл на склад (без сортировки)» - 
        Открылась форма «Ввод данных о блоке»
4) Нажать кнопку «Продолжить без курьера» - 
    Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
'''

def test_s_8():
    driver = login()

    time.sleep(0.5)

    check_enty(driver)

    time.sleep(0.5)

    check_menu(driver)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

if __name__ == "__main__":
    test_s_8()