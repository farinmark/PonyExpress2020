from event_registration import event_registration
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony
from Menu_button_click import menu_button_click
from log_out import Print

def test_case_13():
    driver = event_registration()
    if driver == "FAIL ON STAGE: Find production button" or driver == "FAIL ON STAGE: Find EventRegistration button":
        driver.close()
        return driver

    try:
        element_included_in_consolidation_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a")))
    except:
        Print("Button included in consolidation wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find include in consolidation button"

    element_included_in_consolidation_button.click()
    Print("Include in consolidation button click")

    time.sleep(0.5)
    driver.switch_to_window(driver.window_handles[1])

    time.sleep(2)

    try:
        element_menu_is_exist = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/p")))
    except:
        Print("No menu to input")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'FAIL ON STAGE: Find menu'

    try:
        element_choose_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button')))
    except:
        Print("Choose button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find choose button"

    element_choose_button.click()
    Print("Choose button click")

    try:
        element_search_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="search-input"]')))
    except:
        Print("Field to input wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find field to input"

    element_search_field.send_keys("1202")
    Print("1202 was sent in search field")

    try:
        element_first_group_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]')))
    except:
        Print("First group button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find first group button"

    element_first_group_button.click()
    Print("First group button click")
    time.sleep(1)
    try:
        element_add_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]')))
    except:
        Print("Add button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find add button"

    element_add_button.click()

    try:
        element_add_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]/span')))
    except:
        Print("Add button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find add button"

    element_add_button.click()
    Print("Add button click")
    time.sleep(1)

    try:
        element_continue_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button')))
    except:
        Print("Continue button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find continue button"

    element_continue_button.click()
    Print("Continue button click")

    try:
        element_main_menu_name_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[1]/h1')))
    except:
        Print("Didn't out in main menu")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Out in main menu"

    if element_main_menu_name_field.text == '79. Включен в консолидацию':
        Print("Out in main menu")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'Success'
    else:
        Print("Out in different menu")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Out in main menu"

