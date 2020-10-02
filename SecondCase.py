from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    try:
        element_menuButtom = driver.find_element_by_class_name("bp3-button-text")
    except:
        return "Wrong login or password"
    try:
        element_QuitFromPage = driver.find_element_by_xpath("M7 14H2V2h5c.55 0 1-.45 1-1s-.45-1-1-1H1C.45 0 0 .45 0 1v14c0 .55.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1zm8.71-6.71l-3-3a1.003 1.003 0 00-1.42 1.42L12.59 7H6c-.55 0-1 .45-1 1s.45 1 1 1h6.59l-1.29 1.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l3-3c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z")
    except:
        return "Can't click on Quit buttom"
    return"Success"
