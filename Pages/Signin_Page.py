import time

from Action.Perform_Driver_Action import perform_find_element, perform_send_keys, perform_click
from Loactors.Sign_In_Locators import Sign_in_Locators
from Utils.Utils import get_data_from_webelement, verify_webelement_displayed, take_full_screenshot, \
    get_current_url


def enter_password(driver, password):
    password_field = perform_find_element(driver, 'id', Sign_in_Locators.password_field)
    perform_send_keys(password_field,password)
    print(f"Password entered : {get_data_from_webelement(password_field)}")

def click_signin_cta(driver):
    signin = perform_find_element(driver, 'xpath', Sign_in_Locators.sign_in_cta)
    perform_click(signin)

def do_signin(driver,password):
    enter_password(driver,password)
    click_signin_cta(driver)


