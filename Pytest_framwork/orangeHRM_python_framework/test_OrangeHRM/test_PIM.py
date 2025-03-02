import time

from selenium.webdriver.common.by import By
from orangeHRM_python_framework.variable.variable import Employee_firstname, Employee_lastname, Employee_ID


def test_pim(setup):

    driver= setup
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    header= driver.find_element(By.TAG_NAME, "h6").text
    time.sleep(3)
    assert "PIM" in header, "PIM click failed"

# def test_add_employee(setup):
#     driver= setup
    driver.find_element(By.XPATH, "(//button[@type ='button'])[5]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name ='firstName']").send_keys(Employee_firstname)
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@name ='lastName']").send_keys(Employee_lastname)
    time.sleep(4)
    # assert "Employee Id already exists" in driver.page_source, "test failed"
    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[1]").send_keys(Employee_ID)
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
    time.sleep(8)

    # Search Employee

    driver.find_element(By.XPATH, "//a[text() ='Employee List']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "(//input[@ placeholder = 'Type for hints...'])[1]").send_keys(Employee_firstname)
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
    time.sleep(4)

    assert "Record Found" or "Records Found" in driver.find_element(By.XPATH, "(//span[@class = 'oxd-text oxd-text--span'])[1]'"), "test has failed"
    print("Search was successful")

