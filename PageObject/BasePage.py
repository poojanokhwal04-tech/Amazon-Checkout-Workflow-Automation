from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BASEPAGE:

    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    # Methods to get elements
    def visibility_of_element_located(self, locator_variable, locator_value):
        if locator_variable.endswith("_id"):
            return self.wait.until(EC.visibility_of_element_located((By.ID, locator_value)))
        elif locator_variable.endswith("_name"):
            return self.wait.until(EC.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_variable.endswith("_xpath"):
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator_value)))
        else:
            raise ValueError(r'Unsupported locator in the user defined function "visibility_of_element_located" in "C:\Users\Lenovo\PycharmProjects\AMAZON_Checkout_Workflow_Automation\PageObject\BasePage.py": ({locator_variable} = "{locator_value}")')

    def presence_of_element_located(self, locator_variable, locator_value):
        if locator_variable.endswith("_id"):
            return self.wait.until(EC.presence_of_element_located((By.ID, locator_value)))
        elif locator_variable.endswith("_name"):
            return self.wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
        elif locator_variable.endswith("_xpath"):
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        else:
            raise ValueError(r'Unsupported locator in the user defined function "presence_of_element_located" in "C:\Users\Lenovo\PycharmProjects\AMAZON_Checkout_Workflow_Automation\PageObject\BasePage.py": ({locator_variable} = "{locator_value}")')

    def presence_of_all_elements_located(self, locator_variable, locator_value):
        if locator_variable.endswith("_xpath"):
            return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_value)))
        else:
            raise ValueError(r'Unsupported locator in the user defined function "presence_of_all_elements_located" in "C:\Users\Lenovo\PycharmProjects\AMAZON_Checkout_Workflow_Automation\PageObject\BasePage.py": ({locator_variable} = "{locator_value}")')

    # Verification methods
    def text_to_be_present(self, locator_variable, locator_value, text):
        if locator_variable.endswith("_xpath"):
            return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_value)))
        else:
            raise ValueError(r'Unsupported locator in the user defined function "text_to_be_present" in "C:\Users\Lenovo\PycharmProjects\AMAZON_Checkout_Workflow_Automation\PageObject\BasePage.py": ({locator_variable} = "{locator_value}")')

    def title_is(self, title):
        return self.wait.until(EC.title_is(title))

    # Element methods
    def send_keys(self, locator_variable, locator_value, textinput):
        element=self.visibility_of_element_located(locator_variable, locator_value)
        element.clear()
        element.send_keys(textinput)

    def click_on_element(self, locator_variable, locator_value):
        self.visibility_of_element_located(locator_variable, locator_value).click()

    def get_element_text(self, locator_variable, locator_value):
        return self.visibility_of_element_located(locator_variable, locator_value).text

    def is_selected(self, locator_variable, locator_value):
        return self.visibility_of_element_located(locator_variable, locator_value).is_selected()

    def is_enabled(self, locator_variable, locator_value):
        return self.visibility_of_element_located(locator_variable, locator_value).is_enabled()

    def is_displayed(self, locator_variable, locator_value):
        return self.visibility_of_element_located(locator_variable, locator_value).is_enabled()

    def dropdown(self, locator_variable, locator_value, category):
        element=self.presence_of_element_located(locator_variable, locator_value) # we may need to use presence_of_element_located
        s=Select(element)
        s.select_by_visible_text(category)
