from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.cart import CART


class CARTCONFIRMATION:

    def __init__(self,wait, ):
        self.wait=wait

    text_cartconfirmation_xpath = '//h1[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]'
    button_gotocart_xpath = '//a[@href="/cart?ref_=sw_gtc"]'
    button_proceedtobuy_name = 'proceedToRetailCheckout'
    text_cartcount_id='nav-cart-count'

    def verifying_cart_confirmation_page(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_cartconfirmation_xpath), 'Added to cart'))

    def click_on_go_to_cart_button(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_gotocart_xpath))).click()
        return CART(self.wait)

    def click_on_proceed_to_but_on_cart_confirmation_page(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_proceedtobuy_name))).click()

    def get_incremented_value_of_product_quantity_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.text_cartcount_id))).text


