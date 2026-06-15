from PageObject.homepage import HOMEPAGE
import pytest

@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_001_verify_home_page(self):
        homepagetitle= HOMEPAGE(self.wait)
        if homepagetitle.verify_homepage_title()==True:
            assert True
        else:
            self.driver.save_screenshot('ss.png')


