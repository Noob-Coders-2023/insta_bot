from selenium import webdriver
from selenium.webdriver.common.by import By
from info import username, password
import time
from tkinter import *
link = "https://www.instagram.com/"

def start():
    driver = webdriver.Firefox()
    time.sleep(5)
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    login(driver)
def login(driver):
    try:
        btn_cookie = driver.find_element(By.XPATH, "// button[contains(text(), 'only allow essential cookies')]")
        if btn_cookie:
            btn_cookie.click()
            time.sleep(10)
    except:
        time.sleep(5)
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(username)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        btn_login = driver.find_element(By.XPATH, "// div[contains(text(), 'Log in')]")
        btn_login.click()
        time.sleep(10)
        driver.get(link+username)
        time.sleep(10)
        like(driver)

def like(driver):
    btn_like = driver.find_element(By.CSS_SELECTOR, "._aagv")
    btn_like.click()
    print("done")
    time.sleep(5)
    driver.close()


start()