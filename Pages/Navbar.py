from Action.Perform_Driver_Action import perform_find_element, perform_click
from Loactors.Navbar_Locators import Navbar_Locators


def click_navbar_order(driver):
    navbar_order_cta = perform_find_element(driver, "xpath", Navbar_Locators.order)
    perform_click(navbar_order_cta)