from selenium.common import TimeoutException
from PageObject.homepage import HOMEPAGE
from PageObject.signinpage import SIGNIN
from Utilities import ReadExcelFile
from TestCase.BaseTest import BASETEST
import pytest

class TestSignInInputs(BASETEST):

    @pytest.mark.parametrize("username, password", ReadExcelFile.read_excel_file())
    def test_401_using_different_inputs_in_sign_in_fields(self, username, password):
        signin = SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number(username)
        try:
            signin.enter_password(password)
        except TimeoutException:
            pass