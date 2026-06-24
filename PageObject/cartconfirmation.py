from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.cart import CART


class CARTCONFIRMATION:

    def __init__(self,driver,wait, ):
        self.driver=driver
        self.wait=wait

    text_cartconfirmation_xpath = '//h1[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]'
    # input_addtocart_xpath='(//input[@type="submit"])[3]'
    button_gotocart_xpath = '//a[@href="/cart?ref_=sw_gtc"]'
    button_proceedtobuy_name = 'proceedToRetailCheckout'
    text_cartcount_id='nav-cart-count'
    text_subtotal_xpath='(//span[@class="a-price-whole"])[1]'
    img_productclick_xpath='(//img[@class="sw-product-image"])[1]'

    def verifying_cart_confirmation_page(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_cartconfirmation_xpath), 'Added to cart'))

    def click_on_go_to_cart_button(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_gotocart_xpath))).click()
        return CART(self.driver,self.wait)

    def click_on_proceed_to_but_on_cart_confirmation_page(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_proceedtobuy_name))).click()

    def get_incremented_value_of_product_quantity_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.text_cartcount_id))).text

    # def click_on_add_to_cart_on_cart_confirm_page(self):
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_addtocart_xpath))).click()

    def get_subtotal(self):
        subtotal= self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_subtotal_xpath))).text
        return int(subtotal.replace(",", ""))

    def click_on_a_new_product_below(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.img_productclick_xpath))).click()
