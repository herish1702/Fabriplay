import os    
def get_current_url(driver):
    return driver.current_url

def get_data_from_webelement(webelement):
    return webelement.get_attribute("value")

def take_full_screenshot(driver):
    browser_name = driver.capabilities['browserName'].lower()
    save_path = "/Users/macbook/My Stuffs/My Learnings/Automation/Fabriplay/Screenshots"
    base_filename = f"{browser_name}_screenshot.png"
    full_path = os.path.join(save_path, base_filename)
    count = 1
    while os.path.exists(full_path):
        full_path = os.path.join(save_path, f"{browser_name}_screenshot{count}.png")
        count += 1
    driver.save_screenshot(full_path)

def verify_webelement_displayed(webelement):
    return webelement.is_displayed()


