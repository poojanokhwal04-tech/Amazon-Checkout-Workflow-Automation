from PageObject.homepage import HOMEPAGE
from TestCase.BaseTest import BASETEST

class TestHomePage(BASETEST):

    def test_001_verify_home_page(self):
        homepagetitle= HOMEPAGE(self.driver,self.wait)
        self.assertion(homepagetitle.verify_homepage_title(), "Homepage Verification failed")