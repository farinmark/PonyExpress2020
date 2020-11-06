import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony
from Menu_button_click import menu_button_click
from log_out import Print


def event_registration():
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
    return driver