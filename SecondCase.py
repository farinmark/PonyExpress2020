from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def SecondCase():
    driver_path = r'C:\Users\User\Desktop\python\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://pegasus-edu.pegasus.ponyex.local/')
    if driver.title != "Пегас":
        return "Page not found"

    element_login = driver.find_element_by_name("login")
    element_password = driver.find_element_by_name("password")
    element_buttom = driver.find_element_by_class_name("css-1hnkt5t")

    element_login.send_keys("ext.mgu_education")
    element_password.send_keys("rg#P5hZm4F")
    element_buttom.click()

    time.sleep(5)

    try:
        element_menuButtom = driver.find_element_by_class_name("bp3-button-text")
    except:
        driver.close()
        return "Wrong login or password"
    time.sleep(10)
    try:
        element_QuitFromPage = driver.find_element_by_xpath("/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]/span/svg")
        element_QuitFromPage.click()
    except:
        driver.close()
        return "Can't click on Quit buttom"
    driver.close()
    return"Success"
