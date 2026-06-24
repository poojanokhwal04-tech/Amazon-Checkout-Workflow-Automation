from PageObject.signinpage import SIGNIN
from TestCase.BaseTest import BASETEST

class TestSignIn(BASETEST):

    def test_201_verify_sign_in_page(self):
        signin = SIGNIN(self.driver, self.wait)
        signin.open_sign_in_page()
        assert signin.verifying_sign_in_page(), "Sign-in Page verification failed"

    def test_202_sign_in_with_valid_credentials(self):
        signin = SIGNIN(self.driver, self.wait)
        homepage=signin.sign_in_with_valid_credentials()
        assert homepage.verify_sign_in(), "Sign-in Failed"

    def test_203_sign_in_with_no_input(self):
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('')
        assert signin.verify_warning_message_for_no_input(), "Warning message for no input didn't display"

    def test_204_sign_in_with_invalid_email(self):
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('poojanokhwal')
        assert signin.verify_warning_message_for_invalid_email(), "Warning message for invalid email didn't display"

    def test_205_sign_in_with_invalid_mobile_number(self):
        signin=SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('12345')
        assert signin.verify_warning_message_for_invalid_mobile_number(), "Warning message for invalid mobile number didn't display"

    def test_206_sign_in_with_wrong_email_or_mobile_number_or_password(self):
        signin = SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number('pooja04@gmail.com')
        signin.enter_password('Pooj@2004')
        assert signin.verify_warning_message_for_wrong_email_or_password(), "Warning message for wrong email or mobile number or password didn't display"
