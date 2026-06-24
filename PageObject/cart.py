from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BASEPAGE
from PageObject.checkout import CHECKOUT

class CART(BASEPAGE):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    text_shoppingcart_xpath='//h2[@id="sc-active-items-header"]'
    spanbutton_increasequantity_xpath='//span[@data-a-selector="increment-icon"]'
    spanbutton_decreasequantity_xpath='//span[@data-a-selector="decrement-icon"]'
    text_productQuantity_xpath='//span[@data-a-selector="inner-value"]'
    button_deleteproductincart_xpath='//input[@value="Delete"]'
    text_confirmdeletion_xpath='//span[contains(.,"was removed from Shopping Cart")]'
    text_emptycart_xpath='//h3[@class="a-size-large a-spacing-top-base sc-your-amazon-cart-is-empty"]'
    button_proceedtobuy_name='proceedToRetailCheckout'
    checkbox_containgifts_xpath='(//i[@class="a-icon a-icon-checkbox"])[1]'
    text_subtotal_xpath='//span[@class="a-size-medium a-color-base sc-price sc-white-space-nowrap"]'

    def verifying_cart_page(self):
        return self.text_to_be_present('text_shoppingcart_xpath', self.text_shoppingcart_xpath, 'Shopping Cart')

    def get_product_quantity_number(self):
        return self.get_element_text('text_productQuantity_xpath', self.text_productQuantity_xpath)

    def click_on_increase_quantity_of_product(self):
        self.click_on_element('spanbutton_increasequantity_xpath', self.spanbutton_increasequantity_xpath)

    def click_on_decrease_quantity_of_product(self):
        self.click_on_element('spanbutton_decreasequantity_xpath', self.spanbutton_decreasequantity_xpath)

    def click_on_delete_to_delete_all_products_from_cart(self):
        ln = len(self.presence_of_all_elements_located('button_deleteproductincart_xpath', self.button_deleteproductincart_xpath))
        for _ in range(0,ln):
            (self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.button_deleteproductincart_xpath))))[0].click()
            text = self.get_element_text('text_confirmdeletion_xpath', self.text_confirmdeletion_xpath)
            if "was removed from Shopping Cart" not in text:
                return False
        return True

    def verifying_deletion_all_products_from_cart(self):
        self.driver.refresh()
        sleep(2)
        return self.text_to_be_present('text_emptycart_xpath', self.text_emptycart_xpath, "Your Amazon Cart is empty")

    def click_on_this_order_contains_gift_checkbox(self):
        self.click_on_element('checkbox_containgifts_xpath', self.checkbox_containgifts_xpath)

    def get_subtotal_price(self):
        subtotal = self.get_element_text('text_subtotal_xpath', self.text_subtotal_xpath)
        return int(float(subtotal.replace("₹", "").replace(",", "")))

    def click_on_proceed_to_buy_on_cart_page(self):
        self.click_on_element('button_proceedtobuy_name', self.button_proceedtobuy_name)
        return CHECKOUT(self.driver, self.wait)