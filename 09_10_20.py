import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pony_driver_init(driver_path):
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

def authorization_in_pony(driver_path, Login, Password):
    driver = pony_driver_init(driver_path)
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


def first_case(driver_path, Login, Password):
    driver = authorization_in_pony(driver_path, Login, Password)
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    else:
        print("Case 1 success")
        driver.close()
        return "Success"

def second_case(driver_path, Login, Password):
    driver = authorization_in_pony(driver_path, Login, Password)
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    try:
        element_exit_buttom = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
    except:
        print("No \"EXIT\" buttom")
        driver.close()
        return "FAIL ON STAGE: Find exit buttom"

    element_exit_buttom.click()

    try:
        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        print("Authorization page was't opened")
        driver.close()
        return "Authorization page was't opened"
    print("Case 2 success")
    driver.close()
    return "Success"

def third_case(driver_path, Login, Password):
    driver = pony_driver_init(driver_path)
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

    try:
        element_infoplate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))
    except:
        print("No plate about wrong login or password")
        driver.close()
        return "FAIL"
    print("Case 3 success")
    driver.close()
    return "Success"

def fifth_case(driver_path, Login, Password):
    driver = authorization_in_pony(driver_path, Login, Password)
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    else:
        print("Authorization success")

    element_menu_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    element_menu_button.click()
    try:
        element_servise_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a/div')))
    except:
        print("No tab after menu button click")
        driver.close()
        return "FAIL ON STAGE: Click menu button"

    print("Menu button click")
    element_servise_button.click()

    try:
        element_Permissions_management_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a/div')))
    except:
        print("No tab after servise button click")
        driver.close()
        return "FAIL ON STAGE: Click servise button"

    print("Servis button click")
    element_Permissions_management_button.click()

    try:
        element_Group_of_users_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a/div')))
    except:
        print("No tab after Permissions management click")
        driver.close()
        return "FAIL ON STAGE: Click Permissions management button"

    print("Permissions management button click")
    element_Group_of_users_button.click()

    try:
        element_key_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]/span[2]')))
    except:
        print("No page after group of users button click")
        driver.close()
        return "FAIL ON STAGE: Click group of users button button"

    print("Group of users click")

    print("Case 5 success")
    driver.close()
    return "Success"

def menu_button_click(driver_path, Login, Password):
    driver = authorization_in_pony(driver_path, Login, Password)
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page":
        return driver
    else:
        print("Authorization success")

    element_menu_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    element_menu_button.click()
    try:
        element_servise_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a/div')))
    except:
        print("No tab after menu button click")
        driver.close()
        return "FAIL ON STAGE: Click menu button"

    print("Menu button click")
    return driver

def sixth_case(driver_path, Login, Password):
    driver = menu_button_click(driver_path, Login, Password)
    if driver == "FAIL ON STAGE: Wrong login or password" or driver == "No such input fields" or driver == "FAIL ON STAGE: Open page" or driver == "FAIL ON STAGE: Click menu button":
        return driver

    element_servise_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a/div')))

    element_servise_button.click()

    try:
        element_Permissions_management_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a/div')))
    except:
        print("No tab after servise button click")
        driver.close()
        return "FAIL ON STAGE: Click servise button"

    print("Servis button click")
    element_Permissions_management_button.click()

    try:
        element_Group_of_users_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a/div')))
    except:
        print("No tab after Permissions management click")
        driver.close()
        return "FAIL ON STAGE: Click Permissions management button"

    print("Permissions management button click")
    element_Group_of_users_button.click()

    try:
        element_create_group_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]')))
    except:
        print("No page after group of users button click")
        driver.close()
        return "FAIL ON STAGE: Click group of users button button"

    print("Group of users click")

    element_create_group_button.click()
    try:
        element_create_group_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input')))
    except:
        print("No create group window")
        driver.close()
        return "FAIL ON STAGE: Click on create group button "

    element_create_group_name_field.send_keys(Password)
    element_save_group_name_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]/span')))
    element_save_group_name_button.click()
    try:
        element_search_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input')))
    except:
        print("Save group button wasn't cliked")
        driver.close()
        return "FAIL ON STAGE: Click on save group button"
    element_search_field.send_keys(Password)
    element_page_counter =  WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[2]/div[1]/span/strong')))
    Page_counter = element_page_counter.text
    if Page_counter == "1 из 1":
        print("Group create success")
    else:
        print("Group wasn't created")
        driver.close()
        return "FAIL ON STAGE: Create group"
    print("6 case success")
    driver.close()
    return "success"


if __name__ == "__main__":
    Login = "ext.mgu_education"
    Password = "rg#P5hZm4F"
    driver_path = r'C:\Users\User\Desktop\python\chromedriver.exe'
    sixth_case(driver_path, Login, Password)