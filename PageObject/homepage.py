from PageObject.BasePage import BASEPAGE
from PageObject.cart import CART
from PageObject.searchresults import SEARCHRESULTS
from Utilities.ReadSearchData import searchitem, searchcategory

class HOMEPAGE(BASEPAGE):

    def __init__(self, driver, wait):
        super().__init__(driver,wait)

    button_signin_xpath='//span[@id="nav-link-accountList-nav-line-1"]'
    textarea_searchbox_id='twotabsearchtextbox'
    dropdown_searchcategory_id='searchDropdownBox'
    button_search_id='nav-search-submit-button'
    text_cartcount_id='nav-cart-count'
    text_confirmsignin_xpath='//span[text()="Hello, Pooja"]'

    def verify_homepage_title(self):
        return self.title_contains("Amazon.in")

    def verify_sign_in(self):
        return self.text_to_be_present('text_confirmsignin_xpath', self.text_confirmsignin_xpath,"Hello, Pooja")

    def click_on_cart_icon(self):
        self.click_on_element('text_cartcount_id', self.text_cartcount_id)
        return CART(self.driver, self.wait)

    def click_on_sign_in_link(self):
        self.click_on_element('button_signin_xpath', self.button_signin_xpath)

    def enter_data_in_searchbox(self, productname):
        self.send_keys('textarea_searchbox_id',self.textarea_searchbox_id, productname)

    def apply_category_for_searching_item(self, category):
        self.dropdown('dropdown_searchcategory_id', self.dropdown_searchcategory_id, category)

    def click_on_search_button(self):
        self.click_on_element('button_search_id', self.button_search_id)

    def search_for_an_item(self):
        self.enter_data_in_searchbox(searchitem)
        self.apply_category_for_searching_item(searchcategory)
        self.click_on_search_button()
        return SEARCHRESULTS(self.driver, self.wait)