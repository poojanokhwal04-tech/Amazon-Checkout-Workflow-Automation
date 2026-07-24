from PageObject.signinpage import SIGNIN
from TestCase.BaseTest import BASETEST

class TestSignIn(BASETEST):

    def test_201_verify_sign_in_page(self): # FT-001: Sign-in page verification
        signin = SIGNIN(self.driver, self.wait)
        signin.open_sign_in_page()
        self.assertion(signin.verifying_sign_in_page(), "Sign-in Page verification failed")

    def test_202_sign_in_with_valid_credentials(self): # FT-002: Sign-in with valid credentials
        signin = SIGNIN(self.driver, self.wait)
        homepage=signin.sign_in_with_valid_credentials()
        self.assertion(homepage.verify_sign_in(), "Sign-in Failed")

    def test_203_sign_in_with_no_input(self): # FT-003: Sign-in with no input
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('')
        self.assertion(signin.verify_warning_message_for_no_input(), "Warning message for no input didn't display")

    def test_204_sign_in_with_invalid_email(self): # FT-004: Sign-in with invalid email
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('poojanokhwal')
        self.assertion(signin.verify_warning_message_for_invalid_email(), "Warning message for invalid email didn't display")

    def test_205_sign_in_with_invalid_mobile_number(self): # FT-005: Sign-in with invalid mobile number
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('12345')
        self.assertion(signin.verify_warning_message_for_invalid_mobile_number(), "Warning message for invalid mobile number didn't display")

    def test_206_sign_in_with_wrong_email_or_mobile_number_or_password(self): # FT-006: Sign-in with wrong email or mobile number
        signin = SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('pooja04@gmail.com')
        signin.enter_password('Pooj@2004')
        self.assertion(signin.verify_warning_message_for_wrong_email_or_password(), "Warning message for wrong email or mobile number or password didn't display")