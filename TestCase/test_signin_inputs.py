from time import sleep

from selenium.common import TimeoutException
from PageObject.signinpage import SIGNIN
from PageObject.homepage import HOMEPAGE
from Utilities import ReadExcelFile
import pytest

@pytest.mark.usefixtures('setup')
class TestSignInInputs:

    @pytest.mark.parametrize("username, password", ReadExcelFile.read_excel_file())
    def test_401_using_different_inputs_in_sign_in_fields(self, username, password):
        signin = SIGNIN(self.driver,self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number(username)
        if signin.verifying_sign_in_page()==True:
            pass
        elif signin.verify_password_page()==True:
            assert signin.enter_password(password)

