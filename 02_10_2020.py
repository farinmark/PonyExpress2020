from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def FirstCase():
    driver_path = r'C:\Users\User\Desktop\python\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://pegasus-edu.pegasus.ponyex.local/')

    element_login = driver.find_element_by_name("login")
    element_password = driver.find_element_by_name("password")
    element_buttom = driver.find_element_by_class_name("css-1hnkt5t")

    element_login.send_keys("ext.mgu_education")
    element_password.send_keys("rg#P5hZm4F")
    element_buttom.click()

    try:
        element_menuButtom = driver.find_element_by_class_name("bp3-button-text")
    except:
        return "Wrong login or password"
    try:
        element_Wrong = driver.find_element_by_class_name("css-hnp1e7")
    except:
        return "Success"
