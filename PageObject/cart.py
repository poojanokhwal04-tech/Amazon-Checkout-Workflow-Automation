from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.checkout import CHECKOUT


class CART:

    def __init__(self, driver, wait):
        self.driver=driver
        self.wait=wait

    text_shoppingcart_xpath='//h2[@id="sc-active-items-header"]'
    text_productname_xpath='(//span[@class="a-truncate-full a-offscreen"])[5]'
    # text_cart_xpath='(//span[@class="a-truncate-full"])[1]'
    spanbutton_increasequantity_xpath='//span[@data-a-selector="increment-icon"]'
    spanbutton_decreasequantity_xpath='//span[@data-a-selector="decrement-icon"]'
    checkbox_selectrpoduct_xpath='//span[@class="a-label a-checkbox-label"]'
    text_productQuantity_xpath='//span[@data-a-selector="inner-value"]'
    button_deleteproductincart_xapth='//input[@value="Delete"]'
    text_confirmdeletion_xpath='//span[contains(.,"was removed from Shopping Cart")]'
    text_emptycart_xpath='//h3[@class="a-size-large a-spacing-top-base sc-your-amazon-cart-is-empty"]'
    button_proceedtobuy_name='proceedToRetailCheckout'
    checkbox_containgifts_xpath='(//i[@class="a-icon a-icon-checkbox"])[1]'
    text_totalprice_id='sc-subtotal-amount-buybox'
    text_subtotal_xpath='//span[@class="a-size-medium a-color-base sc-price sc-white-space-nowrap"]'

    def verifying_cart_page(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH,self.text_shoppingcart_xpath),'Shopping Cart'))

    def get_product_name_added_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_productname_xpath))).text

    def get_product_quantity_number(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_productQuantity_xpath))).text

    def click_on_increase_quantity_of_product(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.spanbutton_increasequantity_xpath))).click()

    def click_on_decrease_quantity_of_product(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.spanbutton_decreasequantity_xpath))).click()

    def click_on_product_selection_checkbox(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.checkbox_selectrpoduct_xpath))).click()

    def click_on_delete_to_delete_all_products_from_cart(self):
        ln = len(self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.button_deleteproductincart_xapth))))
        for _ in range(0,ln):
            (self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.button_deleteproductincart_xapth))))[0].click()
            text=self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_confirmdeletion_xpath))).text
            if "was removed from Shopping Cart" not in text:
                return False
        return True

    def verifying_deletion_all_products_from_cart(self):
        self.driver.refresh()
        sleep(2)
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH,self.text_emptycart_xpath), "Your Amazon Cart is empty"))

    def click_on_this_order_contains_gift_checkbox(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.checkbox_containgifts_xpath))).click()

    def get_total_price_of_selected_items_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_totalprice_id))).text

    def get_subtotal_price(self):
        subtotal=self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_subtotal_xpath))).text
        return int(float(subtotal.replace("₹", "").replace(",", "")))

    def click_on_gifts_checkbox(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.checkbox_containgifts_xpath))).click()

    def click_on_proceed_to_buy_on_cart_page(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME,self.button_proceedtobuy_name))).click()
        return CHECKOUT(self.wait)