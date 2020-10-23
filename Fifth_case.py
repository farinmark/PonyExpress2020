import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony

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