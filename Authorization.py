import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Pathes

def pony_driver_init():
    driver_path = Pathes.driver_path
    pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(pegas_url)
    try:
        title = WebDriverWait(driver, 10).until(EC.title_is("Пегас"))
    except:
        print("Page wasn't open")
        driver.close()
        return "Page wasn't open"
    print("Page was opened")
    time.sleep(5)
    return driver

def authorization_in_pony():
    Login = Pathes.Login
    Password = Pathes.Password
    driver = pony_driver_init()
    if driver == "Page wasn't open":
        return "FAIL ON STAGE: Open page"
    try:
        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        print("No such input fields")
        driver.close()
        return "No such input fields"
    element_login.send_keys(Login)
    element_password.send_keys(Password)

    element_buttom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/button')))
    element_buttom.click()

    time.sleep(5)

    try:
        element_menu_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    except:
        print("Wrong login or password")
        driver.close()
        return "FAIL ON STAGE: Wrong login or password"
    print("Success authorization")
    return driver