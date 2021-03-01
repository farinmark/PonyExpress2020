import time
from login_page import login
from included_in_consolidation import input_dote_name
from included_in_consolidation import choose_the_first_group
from included_in_consolidation import continue_button
from included_in_consolidation import check_menu
from included_in_consolidation import full_screen_button
from included_in_consolidation import check_colour_full_screen
from included_in_consolidation import enter_object_name_full_screen
import pytest

'''
Тест-кейс №15. Работа блока событий 79 в полноэкранном режиме
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
8) Нажать кнопку «Полноэкранный режим» -
    Открывается окно с одним полем ввода
9) В поле «Ввод данных» ввести текст «99-9999-9999/999» и нажать Enter - 
    Поле ввода стало красным
'''

def test_s_15():
    driver = login()

    time.sleep(0.5)

    input_dote_name(driver, '1202')

    time.sleep(2)

    choose_the_first_group(driver)

    time.sleep(0.5)

    continue_button(driver)

    time.sleep(2)

    check_menu(driver)

    time.sleep(0.5)

    full_screen_button(driver)

    time.sleep(0.5)

    enter_object_name_full_screen(driver, '99-9999-9999/999')

    time.sleep(0.5)

    back_ground_colour = check_colour_full_screen(driver)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    assert back_ground_colour == 'background-color: rgb(194, 48, 48);', 'Рамка стала другого цвета'

if __name__ == "__main__":
    test_s_15()