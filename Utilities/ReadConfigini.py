from configparser import ConfigParser

def read_configuration_file(category,key):
    configurations=ConfigParser()
    configurations.read("C:\\Users\\Lenovo\\PycharmProjects\\AMAZON_Checkout_Workflow_Automation\\Configurations\\config.ini")
    return configurations.get(category,key)