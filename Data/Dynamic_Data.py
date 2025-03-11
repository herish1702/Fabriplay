from datetime import datetime, timedelta

def get_date(days_to_add):
    current_date = datetime.now().date()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime('%d-%m-%Y')
    return formatted_future_date

class dynamic_data:
    user_name = '9629798904'
    password = 'Thiruppuvanam20@'
    client_number = '9122317756'
    client_name = 'Dingi'
    client_address = '1, Wallahjah Rd, Chepauk, Triplicane, Chennai, Tamil Nadu 600002'
    client_reference = 'Instagram'
    product_count = 2
    product_name = 'Shirt'
    delivery_date = get_date(7)
    product_amount = '1697'
    advance_amount = '950'

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


