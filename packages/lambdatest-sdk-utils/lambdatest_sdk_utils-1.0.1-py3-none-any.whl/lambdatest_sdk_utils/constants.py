import os

def get_smart_ui_server_address():
    if not os.getenv('SMARTUI_SERVER_ADDRESS'):
        raise Exception('SmartUI server address not found')
    return os.getenv('SMARTUI_SERVER_ADDRESS')

def get_pkg_name():
    return "@lambdatest/python-selenium-driver"