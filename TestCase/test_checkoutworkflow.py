from PageObject.checkout import CHECKOUT
from PageObject.homepage import HOMEPAGE
from PageObject.signinpage import SIGNIN
from TestCase.BaseTest import BASETEST
from Utilities import ReadCredentials
from time import sleep

class TestCheckoutFlow(BASETEST):

    def test_301_before_sign_in(self): # E2E-001: Complete Checkout Using COD, E2E-010: Existing Address Checkout, E2E-015: Gift Option Checkout
        signin = SIGNIN(self.driver, self.wait)
        homepage=HOMEPAGE(self.driver, self.wait)
        username, password = ReadCredentials.get_credentials()

        searchresults = homepage.search_for_an_item()
        self.assertion(searchresults.verify_search_results_page(), "Search Result Page Verification failed")
        product = searchresults.click_on_one_of_the_results()
        product.switch_to_product_details_child_browser()
        self.assertion(product.verify_product_details_page(), "Product details page didn't appear: Failed")
        cartconfirm = product.add_product_to_cart_on_product_details_page()

        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")
        cart.click_on_this_order_contains_gift_checkbox()
        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        self.assertion(signin.verifying_sign_in_page(), "Sign-in failed")
        signin.enter_email_or_phone_number(username)
        signin.enter_password(password)
        self.assertion(checkout.verify_checkout_page(), "Checkout page didn't open")
        assert checkout.verify_checkout_page(), "Checkout page didn't open"
        checkout.click_on_safe_gift_options()
        sleep(2)
        self.assertion(not checkout.verify_if_use_this_payment_method_is_enabled(), " 'Use this payment method' button is enabled but it shouldn't be")
        checkout.click_on_cash_on_delivery()
        sleep(2)
        self.assertion(checkout.verify_selection_of_COD(), "COD radio button didn't get selected")
        self.assertion(checkout.verify_if_use_this_payment_method_is_enabled(), " 'Use this payment method' button enablility couldn't be confirmed")
        checkout.click_on_use_this_payment_method()
        self.assertion(checkout.verify_if_place_oder_button_is_enabled(), " 'Place Order' button didn't get enabled")

    # Pre-requisite: Deselect Gifts option
    def test_302_after_sign_in(self): # E2E-003: Complete Checkout Using UPI / Scan & Pay
        product = self.flow_from_homepage_to_product_details_page()

        cartconfirm = product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")

        self.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_303_using_buy_now_option_on_product_details_page(self): #E2E-002: Complete Checkout Using Net Banking, E2E-004: Buy Now Flow
        product = self.flow_from_homepage_to_product_details_page()

        checkout = product.click_on_buy_now()
        self.assertion(checkout.verify_checkout_page(), "Checkout page didn't open")
        sleep(2)
        self.assertion(not checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button is enabled but it shouldn't be")
        checkout.select_net_bankname_from_dropdown("HDFC Bank")
        sleep(2)
        self.assertion(checkout.verify_selection_of_net_banking(), " 'Net Banking' didn't get selected")
        self.assertion(checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled")
        checkout.click_on_use_this_payment_method()
        checkout.click_on_cross_to_close_popup()
        self.assertion(checkout.verify_if_pay_with_net_banking_is_enabled(), "'Place Order' button didn't get enabled")

    def test_304_increase_decrease_cart_product_quantity(self): # E2E-007: Increase/Decrease Quantity, E2E-013: Verify Price Consistency
        checkout = CHECKOUT(self.driver,self.wait)
        product = self.flow_from_homepage_to_product_details_page()

        priceofproduct = product.get_product_price()
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")

        subtotalbefore = cart.get_subtotal_price()
        before=cart.get_product_quantity_number()
        cart.click_on_increase_quantity_of_product()
        sleep(2)
        cart.click_on_increase_quantity_of_product()
        sleep(4)

        subtotalafterincrease = cart.get_subtotal_price()
        quantityafterincrease=cart.get_product_quantity_number()
        self.assertion(int(quantityafterincrease)==int(before)+2, "Quantity couldn't be increased")
        self.assertion(subtotalafterincrease == subtotalbefore + priceofproduct + priceofproduct,"Subtotal isn't consistent after quantity increase")

        cart.click_on_decrease_quantity_of_product()
        sleep(4)

        subtotalafterdecrease = cart.get_subtotal_price()
        quantityafterdecrease=cart.get_product_quantity_number()
        self.assertion(int(quantityafterdecrease)==int(quantityafterincrease)-1, "Quantity couldn't be decreased")
        self.assertion(subtotalafterdecrease == subtotalafterincrease - priceofproduct,"Subtotal isn't consistent after quantity decrease")

        self.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()
        onlyitemsprice=checkout.get_itemsprice_only()
        self.assertion(onlyitemsprice == subtotalafterdecrease, "Inconsistency in Items Price on Checkout")

    def test_305_delete_cart_product(self): # E2E-008: Delete Product From Cart, E2E-009: Delete All Products From Cart
        product = self.flow_from_homepage_to_product_details_page()
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")

        cart.click_on_delete_to_delete_all_products_from_cart()
        self.assertion(cart.verifying_deletion_all_products_from_cart(), "Product didn't get deleted from the Cart")

    def test_306_adding_product_to_cart_from_search_results_page(self): # E2E-005: Add Product From Search Results
        signin = SIGNIN(self.driver, self.wait)
        homepage = HOMEPAGE(self.driver, self.wait)

        signin.sign_in_with_valid_credentials()
        searchresults = homepage.search_for_an_item()
        self.assertion(searchresults.verify_search_results_page(), "Search Result page verification failed")
        searchresults.click_on_add_to_cart_button_on_search_result_page()
        sleep(3)
        searchresults.click_on_accept_on_add_to_cart_popup()
        cart = homepage.click_on_cart_icon()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")

        self.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_307_add_multiple_products(self): # E2E-006: Multiple Products Checkout,
        product = self.flow_from_homepage_to_product_details_page()

        cartconfirm = product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        subtotal1 = cartconfirm.get_subtotal()
        cartconfirm.click_on_a_new_product_below()

        seconditemprice = product.get_product_price()
        product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        subtotal2=cartconfirm.get_subtotal()

        self.assertion(subtotal2==subtotal1+seconditemprice, "Subtotal is wrong. Product may not get added properly")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")

        self.flow_from_proceed_to_buy_to_checkout_using_scan_and_pay()

    def test_308_use_a_new_address(self): # E2E-011: Select New Address
        product = self.flow_from_homepage_to_product_details_page()
        cartconfirm = product.add_product_to_cart_on_product_details_page()
        self.assertion(cartconfirm.verifying_cart_confirmation_page(), "Product didn't add to cart: Cart Confirmation failed")
        cart = cartconfirm.click_on_go_to_cart_button()
        self.assertion(cart.verifying_cart_page(), "Cart page didn't open")
        checkout = cart.click_on_proceed_to_buy_on_cart_page()
        self.assertion(checkout.verify_checkout_page(), "Checkout page didn't open")
        sleep(2)
        self.assertion(not checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button is enabled but it shouldn't be")

        deliveryaddress=checkout.get_delivery_address()
        Addressline1=checkout.add_new_address()
        self.assertion(Addressline1 in deliveryaddress, "New address couldn't get selecetd properly")

        checkout.click_on_cash_on_delivery()
        sleep(2)
        self.assertion(checkout.verify_selection_of_COD(), "COD radio button didn't get selected")
        self.assertion(checkout.verify_if_use_this_payment_method_is_enabled(), "'Use this payment method' button didn't get enabled")
        checkout.click_on_use_this_payment_method()
        self.assertion(checkout.verify_if_place_oder_button_is_enabled(), "'Place Order' button didn't get enabled")