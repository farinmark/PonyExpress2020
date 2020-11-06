import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import pony_driver_init
import Pathes
from log_out import Print

def third_case():
    driver = pony_driver_init()
    Login = Pathes.Login
    Password = "Wrong password"
    if driver == "Page wasn't open":
        return "FAIL ON STAGE: Open page"
    try:
        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        Print("No such input fields")
        driver.close()
        return "No such input fields"
    element_login.send_keys(Login)
    element_password.send_keys(Password)

    element_buttom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/button')))
    element_buttom.click()

    try:
        element_infoplate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))
    except:
        Print("No plate about wrong login or password")
        driver.close()
        return "FAIL"
    Print("Case 3 success")
    driver.close()
    return "Success"