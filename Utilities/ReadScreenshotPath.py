from datetime import datetime

def screenshotpath(testname):
    date = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    screenshotpath=f"C:\\Users\\Lenovo\\PycharmProjects\\AMAZON_Checkout_Workflow_Automation\\Screenshots\\{testname}_{date}.jpg"
    return screenshotpath