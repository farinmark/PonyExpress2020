import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Authorization import authorization_in_pony
from Menu_button_click import menu_button_click

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
        element_create_group_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
    except:
        print("No page after group of users button click")
        driver.close()
        return "FAIL ON STAGE: Click group of users button button"

    print("Group of users click")
    time.sleep(5)

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

    try:
        element_save_group_name_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]/span')))
    except:
        print("No Save group button")
        driver.close()
        return "FAIL ON STAGE: Save new group"

    element_save_group_name_button.click()

    try:
        element_search_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input')))
    except:
        print("Save group button wasn't cliked")
        driver.close()
        return "FAIL ON STAGE: Click on save group button"

    element_search_field.send_keys(Password)

    try:
        element_find_group = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]")))
    except:
        print("Crated group wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find created group"

    #if element_find_group.text != Password:
     #   print("Find group with looks like name")
      #  driver.close()
       # return "FAIL ON STAGE: Find created group: Find group with looks like name"

    #print("Group was found")

    try:
        element_delete_groop_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]")))
    except:
        print("Delete group button wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find delete group button"

    element_delete_groop_button.click()

    print('Delete group button was clicked')

    try:
        element_delete_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]")))
    except:
        print("Delete button wasn't found")
        driver.close()
        return "FAIL ON STAGE: Find delete button"

    element_delete_button.click()

    print("Delete button was ckicked")
    # time.sleep(5)
    driver.close()
    return  "Success"