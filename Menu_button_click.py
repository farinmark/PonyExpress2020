import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Authorization
from log_out import Print


def menu_button_click():
    driver = Authorization.authorization_in_pony()
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    else:
        Print("Authorization success")

    element_menu_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    element_menu_button.click()
    try:
        element_servise_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a/div')))
    except:
        Print("No tab after menu button click")
        driver.close()
        return "FAIL ON STAGE: Click menu button"

    Print("Menu button click")
    return driver