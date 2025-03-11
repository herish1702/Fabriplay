from Data.Dynamic_Data import dynamic_data
from Driver.Driver_Factory import initialize_driver, initialize_firefox_driver
from Pages.Home_Page import click_login_cta
from Pages.Login_Page import do_login
from Pages.Order_Page import click_create_order
from Pages.Signin_Page import do_signin

driver = initialize_firefox_driver()
click_login_cta(driver)
do_login(driver, dynamic_data.user_name)
do_signin(driver, dynamic_data.password)
click_create_order(driver)
