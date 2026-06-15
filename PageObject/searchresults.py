from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.productdetails import PRODUCTDETAILS


class SEARCHRESULTS:

    def __init__(self,driver, wait):
        self.driver=driver
        self.wait=wait
        
    text_results_xpath='//h2[text()="Results"]'
    div_product_xpath='//div[@data-component-type="s-search-result"]'
    # img_product_xpath='//img[@class="s-image"]'
    text_productname_getattribute_xpath='//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]'
    # text_productprice_xpath='//span[@class="a-price"]'
    # text_rating_xpath='//span[@class="a-icon-alt"]'

    text_addtocart_xpath = '//button[text()="Add to cart"]'
    button_addtocartpopupAccept_xpath='//button[@id="a-autoid-176-announce"]'
    button_addtocartpopupCancel_xpath='//span[@id="a-autoid-191-announce"]'

    #verify search results page
    def verify_search_results_page(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_results_xpath),'Results'))

    # #verify products
    # def ResultProductImg(self):
    #     return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.img_product_xpath)))

    # def click_on_the_first_result(self):
    #     productnameelement = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.text_productname_getattribute_xpath)))
    #     finalproductnameelements = []
    #     for i in range(len(productnameelement)):
    #         productarialabel=productnameelement[i].get_attribute('aria-label')
    #         if 'Sponsored Ad' not in productarialabel:
    #             finalproductnameelements.append(productnameelement[i])
    #         else:
    #             pass
    #     finalproductnameelements[1].click()

    def click_on_the_first_result(self):
        productnameelements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.text_productname_getattribute_xpath)))
        for i in range(len(productnameelements)):
            productarialabel=productnameelements[i].get_attribute('aria-label')
            if 'Sponsored Ad' not in productarialabel:
                productnameelements[i].click()
                break
            else:
                pass
        return PRODUCTDETAILS(self.driver, self.wait)

    # def productname_of_the_product_that_will_clicked(self):
    #     productobj, productnameelement = self.click_on_one_of_the_results()
    #     productname = productnameelement.text
    #     return productname

    # def ResultProductPrice(self):
    #     return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.text_productprice_xpath)))
    # 
    # def ResultProductRatingText(self):
    #     return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.text_rating_xpath)))

    def click_on_add_to_cart_button_on_search_result_page(self):
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.text_addtocart_xpath)))

    #add to cart popup after clicking on 'Add to Cart'
    def click_on_accept_on_add_to_cart_popup(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addtocartpopupAccept_xpath))).click()

    def click_on_cancel_on_add_to_cart_popup(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addtocartpopupCancel_xpath))).click()

