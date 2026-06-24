from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from PageObject.cart import CART
from PageObject.searchresults import SEARCHRESULTS
from Utilities.ReadSearchData import searchitem, searchcategory

class HOMEPAGE:

    def __init__(self, driver, wait):
        self.driver=driver
        self.wait=wait

    # title_of_the_page_xpath="//title[contains(text(), 'Amazon.in')]"
    button_signin_xpath='//span[@id="nav-link-accountList-nav-line-1"]'
    textarea_searchbox_id='twotabsearchtextbox'
    dropdown_searchcategory_id='searchDropdownBox'
    button_search_id='nav-search-submit-button'
    text_cartcount_id='nav-cart-count'
    text_confirmsignin_xpath='//span[text()="Hello, Pooja"]'

    def verify_homepage_title(self):
        return self.wait.until(EC.title_contains("Amazon.in"))

    def verify_sign_in(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_confirmsignin_xpath), "Hello, Pooja"))

    def click_on_cart_icon(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_cartcount_id))).click()
        return CART(self.driver, self.wait)

    def click_on_sign_in_link(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_signin_xpath))).click()

    def enter_data_in_searchbox(self, productname):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.textarea_searchbox_id))).send_keys(productname)

    def apply_category_for_searching_item(self, category):
        categorydd=self.wait.until(EC.presence_of_element_located((By.ID, self.dropdown_searchcategory_id)))
        s=Select(categorydd)
        s.select_by_visible_text(category)

    def click_on_search_button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.button_search_id))).click()

    def search_for_an_item(self):
        self.enter_data_in_searchbox(searchitem)
        self.apply_category_for_searching_item(searchcategory)
        self.click_on_search_button()
        return SEARCHRESULTS(self.driver, self.wait)



