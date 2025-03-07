from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def perform_click(webelement):
    webelement.click()

def perform_send_keys(webelement, data):
    webelement.send_keys(data)

def perform_find_element(driver, locator_type, locator_value):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((getattr(By, locator_type.upper()), locator_value)))
    return driver.find_element(getattr(By, locator_type.upper()), locator_value)

def perform_find_elements(driver,locator_type, locator_value):
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((getattr(By, locator_type.upper()), locator_value)))
    return driver.find_elements(getattr(By, locator_type.upper()), locator_value)
