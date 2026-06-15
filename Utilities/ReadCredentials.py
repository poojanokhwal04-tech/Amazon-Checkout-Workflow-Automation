from Utilities.ReadConfigini import read_configuration_file

def get_credentials():
    username = read_configuration_file("common info", "username")
    password = read_configuration_file("common info", "password")
    return username, password