import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from orangeHRM_python_framework.variable.variable import web_url, username_login, password_url


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(web_url)
    print(driver.title)
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(username_login)
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@name= 'password']").send_keys(password_url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
    time.sleep(5)

    yield driver
    driver.quit()
