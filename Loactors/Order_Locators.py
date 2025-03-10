from Data.Dynamic_Data import dynamic_data


class Order_Locators:
    create_order_cta = "//button[text()='+ Create order']"
    client_number = "//input[@placeholder='Phone number']"
    client_name = "clientName"
    client_address = "address"
    reference_drop_down = "//label[text()='Reference']"
    reference_option = f"//li[text()='{dynamic_data.client_reference}']"
