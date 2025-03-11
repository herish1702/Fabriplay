from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Data.Dynamic_Data import  dynamic_url
from Data.Static_Data import static_data
from Utils.Utils import get_current_url
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def initialize_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver

def initialize_firefox_driver():
    firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")  # Uncomment for headless mode
    # firefox_options.set_preference("detach", True) 
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver
    
def initialize_edge_driver():
    edge_options = EdgeOptions()
    # edge_options.add_argument("--headless")  # Uncomment for headless mode
    # edge_options.set_preference("detach", True) 
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver

def initialize_safari_driver():
    safari_options = SafariOptions()
    # safari_options.add_argument("--headless")  # Uncomment for headless mode
    # safari_options.set_preference("detach", True) 
    driver = webdriver.Safari(options=safari_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver