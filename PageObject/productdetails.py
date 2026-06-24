from PageObject.BasePage import BASEPAGE
from PageObject.cartconfirmation import CARTCONFIRMATION
from PageObject.checkout import CHECKOUT

class PRODUCTDETAILS(BASEPAGE):

    def __init__(self,driver,wait, ):
        super().__init__(driver,wait)
        
    text_productprice_xpath='(//span[@class="a-price-whole"])[1]'
    button_addtocart_xpath='//input[@id="add-to-cart-button"]'
    button_buynow_id='buy-now-button'
    text_instock_xpath='//div[@id="availability"]//span'

    def switch_to_product_details_child_browser(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def add_product_to_cart_on_product_details_page(self):
        self.click_on_element('button_addtocart_xpath', self.button_addtocart_xpath)
        return CARTCONFIRMATION(self.driver, self.wait)

    def click_on_buy_now(self):
        self.click_on_element('button_buynow_id', self.button_buynow_id)
        return CHECKOUT(self.driver, self.wait)

    def verify_product_in_stock(self):
        return self.visibility_of_element_located('text_instock_xpath',self.text_instock_xpath)

    def verify_product_details_page(self):
        return self.is_displayed('button_buynow_id', self.button_buynow_id)

    def get_product_price(self):
        subtotal = self.get_element_text('text_productprice_xpath', self.text_productprice_xpath)
        return int(subtotal.replace(",", ""))



