import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony
from Menu_button_click import menu_button_click
from log_out import Print

def eighth_case():
    driver = menu_button_click()
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page" or driver == "FAIL ON STAGE: Click menu button":
        return driver

    try:
        element_production_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
    except:
        Print("Production button wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find production button"

    element_production_button.click()
    Print("Production button click")

    try:
        element_EventRegistration_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span/a/div')))
    except:
        Print("EventRegistration button wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find EventRegistration button"

    element_EventRegistration_button.click()
    Print("EventRegistration click")

    try:
        element_71NoSort_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a/div')))
    except:
        Print("71NoSort button wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find 71NoSort button"

    element_71NoSort_button.click()
    Print("71NoSort click")

    time.sleep(2)

    driver.switch_to_window(driver.window_handles[1])

    try:
        element_without_courier_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]/span")))
    except:
        Print("Without courier button wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find Without courier button"

    element_without_courier_button.click()

    Print("Without courier button click")

    try:
        element_form_name = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1")))
    except:
        Print("Form name wasn't found")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return "FAIL ON STAGE: Find form name"

    if element_form_name.text != "71. Прибыл на склад (без сортировки)":
        Print("Wrong form was opened")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'FAIL ON STAGE: Check form name'

    Print("Success")

    time.sleep(5)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    return "Success"


