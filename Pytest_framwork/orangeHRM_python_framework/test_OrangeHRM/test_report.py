# Create report
import time

from selenium.webdriver.common.by import By

from orangeHRM_python_framework.variable.variable import Report_Name


def test_report(setup):
    driver = setup
    driver.find_element(By.XPATH,"//a[text()='Reports']").click()
    time.sleep(3)

# Add_reports

    driver.find_element(By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--secondary']").click()
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys(Report_Name)

    dropdown=  driver.find_element(By.XPATH, "//i[@class ='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
    dropdown.click()

    driver.find_element(By.NAME, "Employee Name").click()
    assert "Current Employees Only" in driver.find_element(By.XPATH, "//div[text() ='Current Employees Only']"), "test Failed!"



