import os  
from selenium.webdriver.common.action_chains import ActionChains

def get_current_url(driver):
    return driver.current_url

def get_data_from_webelement(webelement):
    return webelement.get_attribute("value")

def take_full_screenshot(driver):
    browser_name = driver.capabilities['browserName'].lower()
    save_path = "/Users/macbook/My Stuffs/Fabriplay/Screenshots"
    base_filename = f"{browser_name}_screenshot.png"
    full_path = os.path.join(save_path, base_filename)
    count = 1
    while os.path.exists(full_path):
        full_path = os.path.join(save_path, f"{browser_name}_screenshot{count}.png")
        count += 1
    driver.save_screenshot(full_path)

def verify_webelement_displayed(webelement):
    return webelement.is_displayed()

def move_to_element_and_click(driver, webelement):
    actions = ActionChains(driver)
    actions.move_to_element(webelement).click().perform()

def perform_drag_and_drop(driver, source, target):
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
    
def perform_scroll_to(driver,webelement):
    driver.execute_script("arguments[0].scrollIntoView();", webelement)

