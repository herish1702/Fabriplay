from Data.Dynamic_Data import dynamic_data


class Order_Details_Locators:
    upload_cta = "//input[@type='file']"
    submit_cta = "//span[text()='OK']"
    notes = "notes"
    add_sourcing_cta = "//button[text()='+ Add Sourcing']"
    fabric_dropdown = "//label[text()='Fabric']/parent::div//*[name()='svg' and @data-testid='ArrowDropDownIcon']"
    fabric_type = f"//li[text()='{dynamic_data.fabric_type}']"
    sourcing_color_drop_down = "//label[text()='Color']/parent::div//*[name()='svg' and @data-testid='ArrowDropDownIcon']"
    sourcing_color = f"//div[text()='{dynamic_data.fabric_color}']"
    fabric_meter = "sourcing.0.meters"
    fabric_meter_price = "sourcing.0.meterPrice"
    total_field = "//label[text()='Total']/parent::div/descendant::input"
    save_details_cta = "//button[text()='Save Details']"


