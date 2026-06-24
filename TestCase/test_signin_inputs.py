from PageObject.homepage import HOMEPAGE
from PageObject.signinpage import SIGNIN
from Utilities import ReadExcelFile
import pytest

@pytest.mark.usefixtures('setup')
class TestSignInInputs:

    @pytest.mark.parametrize("username, password", ReadExcelFile.read_excel_file())
    def test_401_using_different_inputs_in_sign_in_fields(self, username, password):
        signin = SIGNIN(self.driver,self.wait)
        homepage = HOMEPAGE(self.driver, self.wait)
        signin.open_sign_in_page()
        signin.enter_email_or_phone_number(username)
        if signin.verify_password_page():
            signin.enter_password(password)
