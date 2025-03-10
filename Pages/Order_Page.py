from Action.Perform_Driver_Action import perform_find_element, perform_send_keys, perform_click
from Data.Dynamic_Data import dynamic_data
from Loactors.Order_Locators import Order_Locators
from Pages.Navbar import click_navbar_order
from Utils.Utils import get_data_from_webelement


def click_create_order(driver):
    click_navbar_order(driver)
    perform_find_element(driver, "xpath", Order_Locators.create_order_cta)
    enter_order_details(driver)

def enter_order_details(driver):
    enter_client_number(driver)
    enter_client_name(driver)
    enter_client_address(driver)
    enter_client_reference(driver)


def enter_client_number(driver):
    client_number = perform_find_element(driver, "xpath", Order_Locators.client_number)
    perform_send_keys(client_number, dynamic_data.client_number)
    print(f"Client Number entered : {get_data_from_webelement(client_number)}")

def enter_client_name(driver):
    client_name = perform_find_element(driver, "name", Order_Locators.client_name)
    perform_send_keys(client_name, dynamic_data.client_name)
    print(f"Client Name entered : {get_data_from_webelement(client_name)}")

def enter_client_address(driver):
    client_address = perform_find_element(driver, "name", Order_Locators.client_address)
    perform_send_keys(client_address, dynamic_data.client_address)
    print(f"Client Address entered : {get_data_from_webelement(client_address)}")

def enter_client_reference(driver):
    reference_drop_down = perform_find_element(driver, "xpath", Order_Locators.reference_drop_down)
    perform_click(reference_drop_down)
    reference_option = perform_find_element(driver, "xpath", Order_Locators.reference_option)
    perform_click(reference_option)
    print(f"Reference Option : {get_data_from_webelement(reference_option)}")

