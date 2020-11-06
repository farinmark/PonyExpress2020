import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony
from log_out import Print

def second_case():
    driver = authorization_in_pony()
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    try:
        element_exit_buttom = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
    except:
        Print("No \"EXIT\" buttom")
        driver.close()
        return "FAIL ON STAGE: Find exit buttom"

    element_exit_buttom.click()

    try:
        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        Print("Authorization page was't opened")
        driver.close()
        return "Authorization page was't opened"
    Print("Case 2 success")
    driver.close()
    return "Success"