from Action.Perform_Driver_Action import perform_click, perform_find_element, perform_send_keys
from Data.Dynamic_Data import dynamic_data
from Loactors.Order_Details_Locators import Order_Details_Locators
from Utils.Utils import clear_existing_data, get_data_from_webelement, move_to_element_and_click, move_to_element_and_send, perform_scroll_to

def enter_order_view_details(driver):
    enter_product_measurement(driver)
    enter_sourcing_details(driver)

def add_reference_image(driver):
    upload_cta = perform_find_element(driver, "CSS_SELECTOR", Order_Details_Locators.upload_cta)
    file_path = "/Users/macbook/My Stuffs/Fabriplay/Source/download.jpeg"
    move_to_element_and_send(driver, upload_cta, file_path)

def enter_product_measurement(driver):
    note_field = perform_find_element(driver, "name", Order_Details_Locators.notes)
    perform_send_keys(note_field, dynamic_data.note)

def enter_sourcing_details(driver):
    click_add_sourcing_cta(driver)
    select_fabric_type(driver)
    select_fabric_color(driver)
    enter_fabric_meter(driver)
    enter_fabric_meter_price(driver)
    verify_total(driver)
    click_save_details(driver)

def click_add_sourcing_cta(driver):
    add_sourcing_cta = perform_find_element(driver, "xpath", Order_Details_Locators.add_sourcing_cta)
    perform_click(driver, add_sourcing_cta)

def select_fabric_type(driver):
    fabic_drop_down = perform_find_element(driver, "xpath", Order_Details_Locators.fabric_dropdown)
    move_to_element_and_click(driver, fabic_drop_down)
    fabric_option = perform_find_element(driver, "xpath", Order_Details_Locators.fabric_type)
    move_to_element_and_click(driver, fabric_option)

def select_fabric_color(driver):
    color_drop_down = perform_find_element(driver, "xpath", Order_Details_Locators.sourcing_color_drop_down)
    move_to_element_and_click(driver, color_drop_down)
    color_option = perform_find_element(driver, "xpath",Order_Details_Locators.sourcing_color)
    move_to_element_and_click(driver, color_option)

def enter_fabric_meter(driver):
    fabric_meter_field =perform_find_element(driver, "name", Order_Details_Locators.fabric_meter)
    clear_existing_data(fabric_meter_field)
    perform_send_keys(fabric_meter_field, dynamic_data.fabric_meter)

def enter_fabric_meter_price(driver):
    fabric_meter_price = perform_find_element(driver, "name", Order_Details_Locators.fabric_meter_price)
    clear_existing_data(fabric_meter_price)
    perform_send_keys(fabric_meter_price, dynamic_data.fabric_meter_price)

def verify_total(driver):
    calculated_total = round(float(dynamic_data.fabric_meter) * float(dynamic_data.fabric_meter_price))
    total_field= perform_find_element(driver, "xpath", Order_Details_Locators.total_field)
    displayed_total = int(get_data_from_webelement(total_field))
    if calculated_total == displayed_total:
        print(displayed_total)
    else:
        print(f"Calculated Total : {calculated_total}")
        print(f"Displayed Total : {displayed_total}")

def click_save_details(driver):
    save_details_cta = perform_find_element(driver, "xpath", Order_Details_Locators.save_details_cta)
    perform_scroll_to(driver, save_details_cta)
    perform_click(driver, save_details_cta)



