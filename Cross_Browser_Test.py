from Data.Dynamic_Data import dynamic_data
from Driver.Driver_Factories import initialize_drivers
from Pages.Home_Page import click_login_cta
from Pages.Login_Page import do_login
from Pages.Signin_Page import do_signin
from Utils.Utils import take_full_screenshot, get_current_url

drivers = initialize_drivers()

for browser_name, driver in drivers.items():
    print(f"Running tests on {browser_name}:")

    try:
        click_login_cta(driver)
        do_login(driver, dynamic_data.user_name)
        do_signin(driver, dynamic_data.password)
        print()

    except Exception as e:
        print(f"Error in {browser_name}: {e}")
        take_full_screenshot(driver)
        get_current_url(driver)

    finally:
        driver.close()