from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.cartconfirmation import CARTCONFIRMATION
from PageObject.checkout import CHECKOUT
# from selenium.webdriver.support.select import Select
# from Utilities.ReadSearchData import quantity

class PRODUCTDETAILS:

    def __init__(self,driver,wait, ):
        self.driver=driver
        self.wait=wait
        
    text_productname_xpath='//span[@id="productTitle"]'
    # img_productimage_xpath='//div[@id="imgTagWrapperId"]'
    # text_productrating_xpath='(//span[@class="a-icon-alt"])[1]'
    # text_productPrice_xpath='(//span[@class="a-price-whole"])[1]'
    button_addtocart_xpath='//input[@id="add-to-cart-button"]'
    button_buynow_id='buy-now-button'
    dropdown_quantity_id='//span[@id="a-autoid-10-announce"]'
    text_verify_addtocart_xpath='//h1[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]'
    button_gotocart_xpath='//a[@href="/cart?ref_=sw_gtc"]'
    inputbutton_proceedtobuy_xpath='//input[@name="proceedToRetailCheckout"]'
    text_instock_xpath='//div[@id="availability"]//span'

    def switch_to_product_details_child_browser(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def add_product_to_cart_on_product_details_page(self):
        # quantitydd = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_quantity_id)))
        # s = Select(quantitydd)
        # s.select_by_visible_text(quantity)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addtocart_xpath))).click()
        return CARTCONFIRMATION(self.wait)

    def click_on_buy_now(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_buynow_id))).click()
        return CHECKOUT(self.wait)

    def verify_product_in_stock(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_instock_xpath))).text

    # def switch_to_product_details_child_browser(self):
    #     windows=self.driver.window_handles
    #     self.driver.switch_to.window(windows[1])

    def verify_product_details_page(self):
        productname=self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_productname_xpath))).text
        return self.wait.until(EC.title_is(f"{productname}"))

    # def ProductImg(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH,self.img_productimage_xpath))).is_displayed()
    # 
    # def ProductName(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_productname_xpath))).text
    # 
    # def ProductRating(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_productname_xpath))).text
    # 
    # def ProductPrice(self):
    #     return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_productPrice_xpath))).text

    # def select_quantity_from_dropdown(self):
    #     quantitydd = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_quantity_id)))
    #     s = Select(quantitydd)
    #     s.select_by_visible_text(quantity)


