from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Fabriplay.Data.Dynamic_Data import  dynamic_url
from Fabriplay.Data.Static_Data import static_data
from Fabriplay.Utils.Utils import get_current_url


def initialize_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver