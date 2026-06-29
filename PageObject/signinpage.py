from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BASEPAGE
from PageObject.homepage import HOMEPAGE
from Utilities import ReadCredentials

class SIGNIN(BASEPAGE):

    def __init__(self,driver, wait):
        super().__init__(driver,wait)

    textbox_email_name = 'email'
    button_continue_xpath = '//input[@type="submit"]'
    textbox_password_name = 'password'
    button_signin_xpath = '//input[@type="submit"]'
    text_invalidemail_xpath = '(//div[@class="a-alert-content"])[3]'
    text_invalidmobile_xpath = '(//div[@class="a-alert-content"])[2]'
    text_no_input_xpath = '(//div[@class="a-alert-content"])[1]'
    text_wrongemailorpassword_xpath = '(//i[@class="a-icon a-icon-alert"])[1]//following-sibling::div'

    def verifying_sign_in_page(self):
        return self.title_contains("Amazon Sign-In")

    def enter_email_or_phone_number(self,emailorphone):
        self.send_keys('textbox_email_name', self.textbox_email_name, emailorphone)
        self.click_on_element('button_continue_xpath', self.button_continue_xpath) #continue button click

    def verify_password_page(self):
        return self.title_is("Amazon Sign In")

    def enter_password(self,password):
        self.send_keys('textbox_password_name', self.textbox_password_name, password)
        self.click_on_element('button_signin_xpath', self.button_signin_xpath)  # sign-in button click

    def verify_warning_message_for_invalid_email(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_invalidemail_xpath), "Invalid email address"))

    def verify_warning_message_for_invalid_mobile_number(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_invalidmobile_xpath), "Invalid mobile number"))

    def verify_warning_message_for_no_input(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_no_input_xpath), "Enter your mobile number or email"))

    def verify_warning_message_for_wrong_email_or_password(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_wrongemailorpassword_xpath), "Your password is incorrect"))

    def open_sign_in_page(self):
        homepage = HOMEPAGE(self.driver, self.wait)
        homepage.click_on_sign_in_link()

    def sign_in_with_valid_credentials(self):
        self.open_sign_in_page()
        username, password = ReadCredentials.get_credentials()
        self.enter_email_or_phone_number(username)
        self.enter_password(password)
        return HOMEPAGE(self.driver, self.wait)