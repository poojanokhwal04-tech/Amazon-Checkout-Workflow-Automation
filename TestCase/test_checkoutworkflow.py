from Flows.ForCheckOutFlow import CheckOutFlow
from PageObject.homepage import HOMEPAGE
from PageObject.signinpage import SIGNIN
from Utilities import ReadCredentials
from time import sleep
import pytest

@pytest.mark.usefixtures('setup')
class TestCheckoutFlow:

    def test_301_before_sign_in(self):
        signin = SIGNIN(self.driver, self.wait)
        homepage=HOMEPAGE(self.driver, self.wait)
        username, password = ReadCredentials.get_credentials()

        searchresults = homepage.search_for_an_item()
        assert searchresults.verify_search_results_page()
        product = searchresults.click_on_one_of_the_results()
        product.switch_to_product_details_child_browser()
        assert product.verify_product_details_page(), "Product details page didn't appear: Failed"
        # print(product.verify_product_in_stock()), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()

        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"
        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        assert signin.verifying_sign_in_page(), "Sign-in failed"
        signin.enter_email_or_phone_number(username)
        signin.enter_password(password)
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        sleep(2)
        checkout.click_on_cash_on_delivery()
        sleep(2)
        assert checkout.verify_selection_of_COD(), "COD radio button didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        assert checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled"

    def test_302_after_sign_in(self):
        flowhometoproductdetails = CheckOutFlow(self.driver, self.wait)

        product = flowhometoproductdetails.flow_from_homepage_to_product_details_page()

        # assert product.verify_product_in_stock(), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        flowcarttocheckout = CheckOutFlow(self.driver, self.wait)
        flowcarttocheckout.flow_from_proceed_to_buy_to_checkout_using_COD()

    def test_303_using_buy_now_option_on_product_details_page(self):
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"

        checkout = product.click_on_buy_now()
        assert checkout.verify_checkout_page(), "Checkout page didn't open"

        sleep(2)
        checkout.click_on_cash_on_delivery()
        assert checkout.verify_selection_of_COD(), "COD radio button didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        assert checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled"

    def test_304_increase_decrease_cart_product_quantity(self):
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        before=cart.get_product_quantity_number()
        cart.click_on_increase_quantity_of_product()
        afterIncrease=cart.get_product_quantity_number()
        assert int(afterIncrease)==int(before)+1, "Quantity couldn't be increased"
        sleep(3)
        cart.click_on_decrease_quantity_of_product()
        afterDecrease=cart.get_product_quantity_number()
        assert int(afterDecrease)==int(afterIncrease)-1, "Quantity couldn't be decreased"

        flowcarttocheckout = CheckOutFlow(self.driver, self.wait)
        flowcarttocheckout.flow_from_proceed_to_buy_to_checkout_using_COD()

    def test_305_delete_cart_product(self):
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        cart.click_on_delete_product_from_cart()
        assert cart.verifying_product_deletion_from_cart(), "Product didn't get deleted from the Cart"

    def test_306_adding_product_to_cart_from_search_results_page(self):
        signin = SIGNIN(self.driver, self.wait)
        homepage = HOMEPAGE(self.driver, self.wait)

        signin.sign_in_with_valid_credentials()
        searchresults = homepage.search_for_an_item()
        assert searchresults.verify_search_results_page()
        searchresults.click_on_add_to_cart_button_on_search_result_page()
        searchresults.click_on_accept_on_add_to_cart_popup()
        cart = homepage.click_on_cart_icon()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        flowcarttocheckout = CheckOutFlow(self.driver, self.wait)
        flowcarttocheckout.flow_from_proceed_to_buy_to_checkout_using_COD()

    # def test_307_choose_another_existing_address(self):