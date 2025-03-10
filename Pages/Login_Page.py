from Action.Perform_Driver_Action import perform_find_element, perform_send_keys, perform_click
from Loactors.Login_Locators import Login_Locator
from Utils.Utils import get_data_from_webelement


def enter_username(driver, username):
    user_name_field = perform_find_element(driver, "id", Login_Locator.user_name)
    perform_send_keys(user_name_field, username)
    print(f"Username entered : {get_data_from_webelement(user_name_field)}")

def click_continue_cta(driver):
    continue_cta= perform_find_element(driver, 'xpath', Login_Locator.continue_cta)
    perform_click(continue_cta)

def do_login(driver, username):
    enter_username(driver,username)
    click_continue_cta(driver)
