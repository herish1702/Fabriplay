import random

def select_client_options():
    options = ["WhatsApp", "Instagram", "Others", "Google"]
    return(random.choice(options))

class dynamic_data:
    user_name = '9629798904'
    password = 'Thiruppuvanam20@'
    client_number = '9122317756'
    client_name = 'Dingi'
    client_address = '1, Wallahjah Rd, Chepauk, Triplicane, Chennai, Tamil Nadu 600002'
    client_reference = select_client_options()


class dynamic_url:
    login_url = 'login'
    sign_in_url = 'passwordsignin'
    dashboard = 'dashboard'
    order = 'orders'
    tasks = 'task'
    todays_task = 'todays-task'
    check_appointment = 'order-availability-check'
    appointment = 'appointments'
    design_board = 'design'
    crm = 'crm'
    sourcing = 'sourcings'

