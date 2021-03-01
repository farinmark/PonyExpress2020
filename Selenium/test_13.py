import time
from login_page import login
from included_in_consolidation import input_dote_name
from included_in_consolidation import choose_the_first_group
from included_in_consolidation import continue_button
from included_in_consolidation import check_menu
import pytest

'''
Тест-кейс №13. Создание блока событий 79
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «79. Включен в консолидацию» - 
        Открылась форма «Точка назначения»
4) Нажать кнопку «Выбрать» -
    Открылась форма «Выберите точку назначения»
5) Ввести в поле ввода номер точки «1202» - 
    В таблице с точками отображается точка с введенным номером
6) Выбрать в таблице точку 1202 и нажать кнопку «Добавить - 
    Открылась форма «Точка назначения» с выбранной точкой 1202
7) Нажать кнопку «Далее» -
    Открылась форма «79. Включен в консолидацию» с номером созданного блока и точкой назначения 1202
'''

def test_s_13():
    driver = login()

    time.sleep(0.5)

    input_dote_name(driver, '1202')

    time.sleep(2)

    choose_the_first_group(driver)

    time.sleep(0.5)

    continue_button(driver)

    time.sleep(2)

    check_menu(driver)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

if __name__ == "__main__":
    test_s_13()