import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from orangeHRM_python_framework.variable.variable import web_url, username_login, password_url


def test_login(setup):
    driver=setup
    driver.delete_all_cookies()
    assert "dashboard" in driver.current_url, "login failed!"


