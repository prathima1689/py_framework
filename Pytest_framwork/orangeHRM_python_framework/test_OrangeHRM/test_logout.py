import time
import pytest
from selenium.webdriver.common.by import By
from orangeHRM_python_framework.test_OrangeHRM.test_login import setup


@pytest.fixture
def logout(setup):
    driver=setup
    time.sleep(3)


    driver.find_element(By.CSS_SELECTOR, "ul>li>span>i").click()
    logged_out= driver.find_element(By.CSS_SELECTOR, "ul>li>a[href='/web/index.php/auth/logout']")
    logged_out.click()
    time.sleep(3)

    yield driver
    print("done")


def test_logout(logout): # we need to use test_ to execute this method
    driver=logout
    # assert "login" in driver.current_url, "logout failed!"