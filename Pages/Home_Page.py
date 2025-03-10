from Action.Perform_Driver_Action import perform_find_element, perform_click
from Loactors.Home_Locators import Home_locators


def click_login_cta(driver):
    login_cta = perform_find_element(driver,"xpath",Home_locators.login_cta)
    perform_click(login_cta)