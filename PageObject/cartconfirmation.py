from PageObject.BasePage import BASEPAGE
from PageObject.cart import CART

class CARTCONFIRMATION(BASEPAGE):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    text_cartconfirmation_xpath = '//h1[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]'
    button_gotocart_xpath = '//a[@href="/cart?ref_=sw_gtc"]'
    button_proceedtobuy_name = 'proceedToRetailCheckout'
    text_cartcount_id='nav-cart-count'
    text_subtotal_xpath='(//span[@class="a-price-whole"])[1]'
    img_productclick_xpath='(//img[@class="sw-product-image"])[1]'

    def verifying_cart_confirmation_page(self):
        return self.text_to_be_present('text_cartconfirmation_xpath', self.text_cartconfirmation_xpath,'Added to cart' )

    def click_on_go_to_cart_button(self):
        self.click_on_element('button_gotocart_xpath', self.button_gotocart_xpath)
        return CART(self.driver,self.wait)

    def click_on_proceed_to_but_on_cart_confirmation_page(self):
        self.click_on_element('button_proceedtobuy_name', self.button_proceedtobuy_name)

    def get_incremented_value_of_product_quantity_in_cart(self):
        return self.get_element_text('text_cartcount_id', self.text_cartcount_id)

    def get_subtotal(self):
        subtotal = self.get_element_text('text_subtotal_xpath', self.text_subtotal_xpath)
        return int(subtotal.replace(",", ""))

    def click_on_a_new_product_below(self):
        self.click_on_element('img_productclick_xpath', self.img_productclick_xpath)