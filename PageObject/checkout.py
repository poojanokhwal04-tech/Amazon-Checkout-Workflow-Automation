from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BASEPAGE
from Utilities.ReadAddressData import Country, Full_name, Mobile_number, Pincode, Addressline1, Landmark

class CHECKOUT(BASEPAGE):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    alink_changeaddress_xpath='//a[@aria-label="Change delivery address"]'
    text_addnewaddress_xpath='//a[@id="add-new-address-desktop-sasp-tango-link"]'

    #new address details
    dropdown_country_id='address-ui-widgets-countryCode-dropdown-nativeId'
    dropdown_state_xpath='(//span[@class="a-dropdown-prompt"])[2]'
    text_fullname_id='address-ui-widgets-enterAddressFullName'
    text_mobilenumber_id='address-ui-widgets-enterAddressPhoneNumber'
    text_pincode_id='address-ui-widgets-enterAddressPostalCode'
    text_addressline1_id='address-ui-widgets-enterAddressLine1'
    text_addressline2_id='address-ui-widgets-enterAddressLine2'
    text_landmark_id='address-ui-widgets-landmark'
    checkbox_makethismydefaultaddress_id='address-ui-widgets-use-as-my-default'
    button_usethisaddress_xpath='(//span[@id="checkout-primary-continue-button-id-announce"])[2]'

    text_deliveryaddress_id='deliver-to-address-text'
    text_itemsprice_xpath='//span[@data-shimmer-target="ordertotals-amount"]'

   # Payment methods
    input_usethispaymentmethod_xpath='(//input[@data-csa-c-slot-id="checkout-secondary-continue-payselect"])'
    input_savegiftoptions_xpath='(//input[@type="submit"])[1]'

    radio_netbanking_xpath='(//input[@type="radio"])[3]'
    dropdown_netbanking_name='ppw-bankSelection_dropdown'
    radio_scanpay_xpath='//input[@value="instrumentId=amzn1.pm.pma.upi-VW5pZmllZFBheW1lbnRzSW50ZXJmYWNlOkdlbmVyaWNHdWVzdF9RckNvZGU.QVk0UEVBQThRWEtTSw&isExpired=false&paymentMethod=UnifiedPaymentsInterface&tfxEligible=false"]'
    radio_cashondelivery_xpath='(//input[@type="radio"])[6]' #(//input[@type="radio"])[6]//ancestor::label
    button_paywithnetbanking_xpath = '(//input[@type="submit"])[1]'
    button_placeorder_xpath= '(//input[@type="submit"])[1]' #'//input[@data-testid="secondary-continue-button"]'
    button_popupcross_xpath='//button[@aria-label="Close"]'
    input_paywithupi_xpath='(//input[@type="submit"])[1]'
    button_incrementquantity_xpath='//span[@data-a-selector="increment-icon"]'
    button_decrementquantity_xpath='//span[@data-a-selector="decrement-icon"]'
    button_delivertothisaddress_id = 'checkout-primary-continue-button-id-announce'

    #COD
    def click_on_cash_on_delivery(self):
        self.click_on_element('radio_cashondelivery_xpath', self.radio_cashondelivery_xpath)

    def verify_selection_of_COD(self):
        return self.is_selected('radio_cashondelivery_xpath', self.radio_cashondelivery_xpath)

    #Place order
    def verify_if_place_oder_button_is_enabled(self):
        return self.is_enabled('button_placeorder_xpath', self.button_placeorder_xpath)

    # Scan and Pay
    def click_on_scan_and_pay(self):
        self.click_on_element('radio_scanpay_xpath', self.radio_scanpay_xpath)

    def verify_selection_of_scan_and_pay(self):
        return self.is_selected('radio_scanpay_xpath', self.radio_scanpay_xpath)

    #Pay with UPI button
    def verify_if_pay_with_upi_is_enabled(self):
        return self.is_enabled('input_paywithupi_xpath', self.input_paywithupi_xpath)

    #Use this payment method
    def click_on_use_this_payment_method(self):
        self.click_on_element('input_usethispaymentmethod_xpath', self.input_usethispaymentmethod_xpath)

    def verify_if_use_this_payment_method_is_enabled(self):
        verifybutton = self.presence_of_element_located('input_usethispaymentmethod_xpath', self.input_usethispaymentmethod_xpath).get_attribute("disabled")
        if verifybutton is not None:
            return False
        else:
            return True

    #Net Banking
    def click_on_net_banking(self):
        self.click_on_element('radio_netbanking_xpath', self.radio_netbanking_xpath)

    def select_net_bankname_from_dropdown(self, bankname):
        self.dropdown('dropdown_netbanking_name', self.dropdown_netbanking_name, bankname)

    def verify_selection_of_net_banking(self):
        return self.is_selected('radio_netbanking_xpath', self.radio_netbanking_xpath)

    def click_on_cross_to_close_popup(self):
        self.click_on_element('button_popupcross_xpath', self.button_popupcross_xpath)

    def verify_if_pay_with_net_banking_is_enabled(self):
        return self.is_enabled('button_paywithnetbanking_xpath', self.button_paywithnetbanking_xpath)

    def click_on_safe_gift_options(self):
        self.click_on_element('input_savegiftoptions_xpath', self.input_savegiftoptions_xpath)

    def get_itemsprice_only(self):
        onlyitemsprice = self.get_element_text('text_itemsprice_xpath', self.text_itemsprice_xpath)
        return int(float(onlyitemsprice.replace("₹", "").replace(",", "")))

    # increase and decrease quantity
    def click_on_increase_quantity(self):
        self.click_on_element('button_incrementquantity_xpath',self.button_incrementquantity_xpath)

    def click_on_decrease_quantity(self):
        self.click_on_element('button_decrementquantity_xpath',self.button_decrementquantity_xpath)

    def get_delivery_address(self):
        return self.get_element_text('text_deliveryaddress_id', self.text_deliveryaddress_id)

    #Add New Address
    def click_on_add_new_address(self):
        self.click_on_element('text_addnewaddress_xpath', self.text_addnewaddress_xpath)

    def select_country_from_dropdown(self, country):
        self.dropdown('dropdown_country_id', self.dropdown_country_id, country)

    def enter_full_name(self, name):
        self.send_keys('text_fullname_id', self.text_fullname_id, name)

    def enter_mobile_number(self, mobilenumber):
        self.send_keys('text_mobilenumber_id', self.text_mobilenumber_id, mobilenumber)

    def enter_pin_code(self, pincode):
        self.send_keys('text_pincode_id', self.text_pincode_id, pincode)

    def enter_address_line_1(self, addressline1):
        self.send_keys('text_addressline1_id', self.text_addressline1_id, addressline1)

    def enter_address_line_2(self, addressline2):
        self.send_keys('text_addressline2_id', self.text_addressline2_id, addressline2)

    def enter_landmark(self, landmark):
        self.send_keys('text_landmark_id', self.text_landmark_id, landmark)

    def click_on_make_this_my_default_address_checkbox(self):
        self.click_on_element('checkbox_makethismydefaultaddress_id', self.checkbox_makethismydefaultaddress_id)

    def click_on_delivery_instructions(self):
        self.click_on_element('alink_deliveryinstructions_xpath', self.alink_deliveryinstructions_xpath)

    def click_on_use_this_address(self):
        self.click_on_element('button_usethisaddress_xpath', self.button_usethisaddress_xpath)

    def click_on_deliver_to_this_address(self):
        self.click_on_element('button_delivertothisaddress_id', self.button_delivertothisaddress_id)

    def add_new_address(self):
        self.click_on_change_address()
        self.click_on_add_new_address()
        self.select_country_from_dropdown(Country)
        self.enter_full_name(Full_name)
        self.enter_mobile_number(Mobile_number)
        self.enter_pin_code(Pincode)
        self.enter_address_line_1(Addressline1)
        self.enter_landmark(Landmark)
        self.click_on_make_this_my_default_address_checkbox()
        self.click_on_use_this_address()
        self.click_on_deliver_to_this_address()
        return Addressline1

    def verify_checkout_page(self):
        return self.wait.until(EC.title_is("Place Your Order - Amazon Checkout"))

    def click_on_change_address(self):
        self.click_on_element('alink_changeaddress_xpath', self.alink_changeaddress_xpath)
