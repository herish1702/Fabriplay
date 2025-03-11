from Action.Perform_Driver_Action import perform_find_element, perform_send_keys, perform_click
from Data.Dynamic_Data import dynamic_data
from Loactors.Order_Locators import Order_Locators
from Pages.Navbar import click_navbar_order
from Utils.Utils import get_data_from_webelement, move_to_element_and_click, perform_drag_and_drop, perform_scroll_to


def click_create_order(driver):
    click_navbar_order(driver)
    CTA = perform_find_element(driver, "xpath", Order_Locators.create_order_cta)
    perform_click(CTA)
    enter_order_details(driver)
    add_product_details(driver)
    enter_product_details(driver)
    select_task_for_order(driver)
    enter_payment_details(driver)
    click_place_order(driver)


def enter_order_details(driver):
    enter_client_number(driver)
    enter_client_name(driver)
    enter_client_address(driver)
    enter_client_reference(driver)

def add_product_details(driver):
    delete_icon = perform_find_element(driver, "xpath", Order_Locators.product_delete_icon)
    perform_click(delete_icon)
    add_product_cta = perform_find_element(driver, "xpath", Order_Locators.add_product_cta)
    perform_click(add_product_cta)

def enter_product_details(driver):
    enter_product_name(driver)
    select_product_type(driver)
    enter_delivery_date(driver)
    enter_product_ammount(driver)

def select_task_for_order(driver):
    add_product_cta = perform_find_element(driver, "xpath", Order_Locators.add_product_cta)
    perform_scroll_to(driver, add_product_cta)
    select_cutting_task(driver)
    select_stiching_task(driver)
    select_embroiding_task(driver)
    select_delivery_task(driver)

def enter_payment_details(driver):
    enter_advance_amount(driver)

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
    move_to_element_and_click(driver,reference_drop_down)
    reference_option = perform_find_element(driver, "xpath", Order_Locators.reference_option)
    perform_click(reference_option)


def enter_product_name(driver):
    name_field = perform_find_element(driver, "name", Order_Locators.product_name)
    perform_send_keys(name_field,dynamic_data.product_name)

def select_product_type(driver):
    product_type_drop_down = perform_find_element(driver, "xpath", Order_Locators.product_type_drop_down)
    perform_click(product_type_drop_down)
    product_type_option = perform_find_element(driver, "xpath", Order_Locators.product_type_option)
    perform_click(product_type_option)

def enter_delivery_date(driver):
    delivery_date = perform_find_element(driver, "name", Order_Locators.delivery_date)
    perform_send_keys(delivery_date,dynamic_data.delivery_date)

def enter_product_ammount(driver):
    product_ammount_field = perform_find_element(driver, "name", Order_Locators.product_amount)
    perform_send_keys(product_ammount_field,dynamic_data.product_amount)

def select_cutting_task(driver):
    cutting_task_cta = perform_find_element(driver, "xpath", Order_Locators.cutting_task_cta)
    timeline_bar = perform_find_element(driver, "xpath", Order_Locators.timeline_destination)
    perform_drag_and_drop(driver, cutting_task_cta, timeline_bar)

def select_embroiding_task(driver):
    embroiding_task = perform_find_element(driver, "xpath", Order_Locators.embroiding_task_cta)
    timeline_bar = perform_find_element(driver, "xpath", Order_Locators.timeline_destination)
    perform_drag_and_drop(driver, embroiding_task, timeline_bar)

def select_stiching_task(driver):
    stiching_task = perform_find_element(driver, "xpath", Order_Locators.stiching_task_cta)
    timeline_bar = perform_find_element(driver, "xpath", Order_Locators.timeline_destination)
    perform_drag_and_drop(driver, stiching_task, timeline_bar)

def select_delivery_task(driver):
    stiching_task = perform_find_element(driver, "xpath", Order_Locators.delivery_task_cta)
    timeline_bar = perform_find_element(driver, "xpath", Order_Locators.timeline_destination)
    perform_drag_and_drop(driver, stiching_task, timeline_bar)

def enter_advance_amount(driver):
    advance_payment_field = perform_find_element(driver, "name", Order_Locators.advance_received_field)
    perform_send_keys(advance_payment_field,dynamic_data.advance_amount)

def click_place_order(driver):
    place_order_cta = perform_find_element(driver, "xpath", Order_Locators.place_order_cta)
    perform_click(place_order_cta)


    

