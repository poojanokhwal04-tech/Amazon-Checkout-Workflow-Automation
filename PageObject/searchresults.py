from PageObject.BasePage import BASEPAGE
from PageObject.productdetails import PRODUCTDETAILS

class SEARCHRESULTS(BASEPAGE):

    def __init__(self,driver, wait):
        super().__init__(driver,wait)
        
    text_results_xpath='//h2[text()="Results"]'
    text_productname_getattribute_xpath='//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]'
    text_addtocart_xpath = '//button[text()="Add to cart"]'
    button_addtocartpopupAccept_xpath='(//div[@class="a-row a-size-medium"])[1]//child::button[text()="Add to cart"]'

    def verify_search_results_page(self):
        return self.text_to_be_present('text_results_xpath', self.text_results_xpath, 'Results')

    def click_on_one_of_the_results(self):
        productnameelements = self.presence_of_all_elements_located('text_productname_getattribute_xpath', self.text_productname_getattribute_xpath)
        for i in range(len(productnameelements)):
            productarialabel=productnameelements[i].get_attribute('aria-label')
            if 'Sponsored Ad' not in productarialabel:
                productnameelements[i].click()
                break
            else:
                pass
        return PRODUCTDETAILS(self.driver, self.wait)

    def click_on_add_to_cart_button_on_search_result_page(self):
        self.click_on_element('text_addtocart_xpath', self.text_addtocart_xpath)

    def click_on_accept_on_add_to_cart_popup(self):
        self.click_on_element('button_addtocartpopupAccept_xpath', self.button_addtocartpopupAccept_xpath)

