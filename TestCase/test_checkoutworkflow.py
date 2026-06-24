from Flows.ForCheckOutFlow import CheckOutFlow
from PageObject.checkout import CHECKOUT
from PageObject.homepage import HOMEPAGE
from PageObject.signinpage import SIGNIN
from Utilities import ReadCredentials
from time import sleep
import pytest

@pytest.mark.usefixtures('setup')
class TestCheckoutFlow:

    def test_301_before_sign_in(self): # E2E-001: Complete Checkout Using COD, E2E-010: Existing Address Checkout, E2E-015: Gift Option Checkout
        signin = SIGNIN(self.driver, self.wait)
        homepage=HOMEPAGE(self.driver, self.wait)
        username, password = ReadCredentials.get_credentials()

        searchresults = homepage.search_for_an_item()
        assert searchresults.verify_search_results_page()
        product = searchresults.click_on_one_of_the_results()
        product.switch_to_product_details_child_browser()
        assert product.verify_product_details_page(), "Product details page didn't appear: Failed"
        cartconfirm = product.add_product_to_cart_on_product_details_page()

        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"
        cart.click_on_gifts_checkbox()
        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        assert signin.verifying_sign_in_page(), "Sign-in failed"
        signin.enter_email_or_phone_number(username)
        signin.enter_password(password)
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        checkout.click_on_safe_gift_options()
        assert not checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button is enabled but it shouldn't be"
        sleep(2)
        checkout.click_on_cash_on_delivery()
        sleep(2)
        assert checkout.verify_selection_of_COD(), "COD radio button didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        assert checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled"

    def test_302_after_sign_in(self): # E2E-003: Complete Checkout Using UPI / Scan & Pay,
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()

        # assert product.verify_product_in_stock(), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        flow.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_303_using_buy_now_option_on_product_details_page(self): #E2E-002: Complete Checkout Using Net Banking, E2E-004: Buy Now Flow
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"

        checkout = product.click_on_buy_now()
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        assert checkout.verify_if_use_this_payment_method_is_enabled()==False, "'Use this payment method' button is enabled but it shouldn't be"
        sleep(2)
        checkout.select_net_bankname_from_dropdown("HDFC Bank")
        sleep(5)
        assert checkout.verify_selection_of_net_banking(), " 'Net Banking' didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        checkout.click_on_cross_to_close_popup()
        assert checkout.verify_if_pay_with_net_banking_is_enabled(), "'Place Order' button didn't get enabled"

    def test_304_increase_decrease_cart_product_quantity(self): # E2E-007: Increase/Decrease Quantity, E2E-013: Verify Price Consistency
        checkout = CHECKOUT(self.wait)
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"

        priceofproduct = product.get_product_price()
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        subtotalbefore = cart.get_subtotal_price()
        before=cart.get_product_quantity_number()
        cart.click_on_increase_quantity_of_product()
        sleep(2)
        cart.click_on_increase_quantity_of_product()
        sleep(4)

        subtotalafterincrease = cart.get_subtotal_price()
        quantityafterincrease=cart.get_product_quantity_number()
        assert subtotalafterincrease==subtotalbefore+priceofproduct+priceofproduct
        assert int(quantityafterincrease)==int(before)+2, "Quantity couldn't be increased"

        sleep(3)
        cart.click_on_decrease_quantity_of_product()
        sleep(4)

        subtotalafterdecrease = cart.get_subtotal_price()
        quantityafterdecrease=cart.get_product_quantity_number()
        assert subtotalafterdecrease == subtotalafterincrease-priceofproduct
        assert int(quantityafterdecrease)==int(quantityafterincrease)-1, "Quantity couldn't be decreased"

        flow.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()
        onlyitemsprice=checkout.get_itemsprice_only()
        assert onlyitemsprice == subtotalafterdecrease, "Inconsistency in Items Price on Checkout"

    def test_305_delete_cart_product(self): # E2E-008: Delete Product From Cart, E2E-009: Delete All Products From Cart
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        assert cart.click_on_delete_to_delete_all_products_from_cart()
        # either True or timeoutexception because empty cart text doesn't appear
        assert cart.verifying_deletion_all_products_from_cart(), "Product didn't get deleted from the Cart"

    def test_306_adding_product_to_cart_from_search_results_page(self): # E2E-005: Add Product From Search Results
        signin = SIGNIN(self.driver, self.wait)
        homepage = HOMEPAGE(self.driver, self.wait)

        signin.sign_in_with_valid_credentials()
        searchresults = homepage.search_for_an_item()
        assert searchresults.verify_search_results_page()
        searchresults.click_on_add_to_cart_button_on_search_result_page()
        # we have already given wait. thn why needed extra sleep?
        sleep(2)
        searchresults.click_on_accept_on_add_to_cart_popup()
        cart = homepage.click_on_cart_icon()
        assert cart.verifying_cart_page(), "Cart page didn't open"
        flow = CheckOutFlow(self.driver, self.wait)
        flow.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_307_add_multiple_products(self): # E2E-006: Multiple Products Checkout,
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()
        # assert product.verify_product_in_stock(), "Product isn't available"

        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        subtotal1 = cartconfirm.get_subtotal()
        cartconfirm.click_on_a_new_product_below()
        print(subtotal1)

        seconditemprice = product.get_product_price()
        product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        subtotal2=cartconfirm.get_subtotal()
        print(subtotal1)

        assert subtotal2==subtotal1+seconditemprice, "Subtotal is wrong. Product may not get added properly"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"

        flow.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_308_use_a_new_address(self): # E2E-011: Select New Address
        flow = CheckOutFlow(self.driver, self.wait)
        product = flow.flow_from_homepage_to_product_details_page()

        cartconfirm = product.add_product_to_cart_on_product_details_page()
        assert cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed"
        cart = cartconfirm.click_on_go_to_cart_button()
        assert cart.verifying_cart_page(), "Cart page didn't open"
        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        assert not checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button is enabled but it shouldn't be"

        deliveryaddress=checkout.get_delivery_address()
        Addressline1=checkout.add_new_address()
        assert Addressline1 in deliveryaddress, "New address couldn't get selecetd properly"

        checkout.click_on_cash_on_delivery()
        sleep(2)
        assert checkout.verify_selection_of_COD(), "COD radio button didn't get selected"
        assert checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled"
        checkout.click_on_use_this_payment_method()
        assert checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled"




