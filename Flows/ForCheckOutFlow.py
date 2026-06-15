from time import sleep
from PageObject.cart import CART
from PageObject.signinpage import SIGNIN

class CheckOutFlow:

    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    def flow_from_homepage_to_product_details_page(self):
        signin = SIGNIN(self.driver, self.wait)

        homepage = signin.sign_in_with_valid_credentials()
        assert homepage.verify_sign_in(), "Sign-in failed"
        searchresults = homepage.search_for_an_item()
        assert searchresults.verify_search_results_page(), "Search Results didn't show: Failed"
        product = searchresults.click_on_one_of_the_results()
        product.switch_to_product_details_child_browser()
        assert searchresults.verify_product_details_page(), "Product details page didn't appear: Failed"
        return product

    def flow_from_proceed_to_buy_to_checkout_using_COD(self):
        cart=CART(self.wait)

        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        sleep(2)
        checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_cash_on_delivery()
        sleep(2)
        assert checkout.verify_selection_of_COD(), "COD radio button didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        assert checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled"
