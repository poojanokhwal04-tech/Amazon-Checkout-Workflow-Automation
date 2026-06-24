from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Utilities.ReadAddressData import Country, Full_name, Mobile_number, Pincode, Addressline1, Landmark

class CHECKOUT:

    def __init__(self, wait):
        self.wait=wait

    #secure checkout
    text_checkoutverify_xpath='//a[@id="nav-checkout-title-header-text"]'

    #order summary
    text_itemprice_xpath='(//span[@data-shimmer-target="ordertotals-amount"])[1]'
    text_deliveryprice_xpath ='(//span[@data-shimmer-target="ordertotals-amount"])[2]'
    text_payondeliveryfee_xpath ='(//span[@data-shimmer-target="ordertotals-amount"])[3]'
    text_itemtotal_xpath ='(//span[@data-shimmer-target="ordertotals-amount"])[4]'
    text_freedelivery_xpath ='//td[@class="a-color-success a-text-right"]'
    text_ordertotal_xpath='(//span[@data-shimmer-target="ordertotals-amount"])[5]'

    alink_changeaddress_xpath='//a[@aria-label="Change delivery address"]'
    text_showmoreaddress_xpath = '//span[.="Show more addresses"]'
    radio_2ndaddress_xpath = '(//i[@class="a-icon a-icon-radio"])[2]'
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
    text_city_id='address-ui-widgets-enterAddressCity'
    checkbox_makethismydefaultaddress_id='address-ui-widgets-use-as-my-default'
    alink_deliveryinstructions_xpath='//span[.="Add preferences, notes, access codes and more"]'
    button_addresstypeHOME_xpath='//button[@aria-label="House"]'
    button_addresstypeAPARTMENT_xpath='//button[@aria-label="Apartment"]'
    button_addresstypeBUSINESS_xpath='//button[@aria-label="Business"]'
    button_addresstypeOTHER_xpath='//button[@aria-label="Other"]'
    accordion_weekenedconfirmation_xpath='//h5[.="Can you receive deliveries at this address on weekends?"]'
    button_saturdayNO_xpath='(//button[@name="closed"])[1]'
    button_saturdayYES_xpath='(//button[@name="open"])[1]'
    button_sundayNO_xpath='(//button[@name="closed"])[2]'
    button_sundayYES_xpath='(//button[@name="open"])[2]'
    accordion_additionalinstructions_xpath='//h5[.="Do we need additional instructions to deliver to this address?"]'
    textarea_deliveryinstruction_id='freeTextInstruction-HOUSE'
    button_usethisaddress_xpath='(//span[@id="checkout-primary-continue-button-id-announce"])[2]'
    button_delivertothisaddress_id='checkout-primary-continue-button-id-announce'

    #error messages for wrong new address
    text_errorname_xpath='//div[.="Please enter a name."]'
    text_mobile_xpath = '//div[.="Please enter a phone number so we can call if there are any issues with delivery."]'
    text_pincode_xpath = '//div[.="Please enter a ZIP or postal code."]'
    text_addressline1_xpath = '//div[.="Please enter an address."]'
    text_city_xpath = '(//div[.="Please enter a city name."])[2]'
    text_state_xpath = '(//div[.="Please enter a state, region or province."])[2]'

    #change payment method
    alink_changepaymentmethod_xpath='//a[@aria-label="Change payment method"]'
    input_usethispaymentmethod_xpath='(//input[@data-csa-c-slot-id="checkout-secondary-continue-payselect"])'
    input_savegiftoptions_xpath='(//input[@type="submit"])[1]'

    radio_card_xpath='(//input[@type="radio"])[2]'
    alink_addcarddetails_xpath='//a[text()="Add a new credit or debit card"]'
    textarea_cardnumber_xpath = '//input[@name="addCreditCardNumber"]'
    textarea_nickname_name='ppw-accountHolderName'
    dropdown_expiryMonth_xpath='//span[text()="01"]'
    dropdown_expiryYear_xpath ='//span[text()="2026"]'
    button_cartCancel_xpath='//button[@type="button"]'
    button_cardContinue_xpath='//span[text()="Continue"]'

    radio_netbanking_xpath='(//input[@type="radio"])[3]'
    dropdown_netbanking_name='ppw-bankSelection_dropdown'
    # radio_scanpay_xpath='(//input[@type="radio"])[4]'
    radio_scanpay_xpath='//input[@value="instrumentId=amzn1.pm.pma.upi-VW5pZmllZFBheW1lbnRzSW50ZXJmYWNlOkdlbmVyaWNHdWVzdF9RckNvZGU.QVk0UEVBQThRWEtTSw&isExpired=false&paymentMethod=UnifiedPaymentsInterface&tfxEligible=false"]'
    radio_cashondelivery_xpath='(//input[@type="radio"])[6]' #(//input[@type="radio"])[6]//ancestor::label
    alink_backtocart_xpath='//a[@href="/gp/cart/view.html?ref_=chk_spc_backToCart"]'
    button_paywithupi_xpath='(//input[@type="submit"])[1]'
    button_paywithnetbanking_xpath = '(//input[@type="submit"])[1]'
    button_placeorder_xpath= '(//input[@type="submit"])[1]' #'//input[@data-testid="secondary-continue-button"]'
    button_popupcross_xpath='//button[@aria-label="Close"]'
    input_paywithupi_xpath='(//input[@type="submit"])[1]'
    button_incrementquantity_xpath='//span[@data-a-selector="increment-icon"]'
    button_decrementquantity_xpath='//span[@data-a-selector="decrement-icon"]'

    text_itemsprice_xpath='//span[@data-shimmer-target="ordertotals-amount"]'
    text_deliveryaddress_id='deliver-to-address-text'

    #COD
    def click_on_cash_on_delivery(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_cashondelivery_xpath))).click()

    def verify_selection_of_COD(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_cashondelivery_xpath))).is_selected()

    # Scan and Pay
    def click_on_scan_and_pay(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_scanpay_xpath))).click()

    def verify_selection_of_scan_and_pay(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_scanpay_xpath))).is_selected()

    #Use this payment method
    def click_on_use_this_payment_method(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_usethispaymentmethod_xpath))).click()

    def verify_if_use_this_payment_method_is_enabled(self):
        verifybutton=self.wait.until(EC.presence_of_element_located((By.XPATH, self.input_usethispaymentmethod_xpath))).get_attribute("disabled")
        if verifybutton is not None:
            return False
        else:
            return True
        # print(self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_usethispaymentmethod_xpath))).get_attribute("disabled"))

    #Pay with UPI
    def verify_if_pay_with_upi_is_enabled(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_paywithupi_xpath))).is_enabled()

    #Net Banking
    def select_net_bankname_from_dropdown(self, bankname):
        banknamedd = self.wait.until(EC.visibility_of_element_located((By.NAME, self.dropdown_netbanking_name)))
        s = Select(banknamedd)
        s.select_by_visible_text(bankname)

    def verify_selection_of_net_banking(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_netbanking_xpath))).is_selected()

    def click_on_cross_to_close_popup(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_popupcross_xpath))).click()

    def verify_if_pay_with_net_banking_is_enabled(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_paywithnetbanking_xpath))).is_enabled()

    def click_on_safe_gift_options(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_savegiftoptions_xpath))).click()

    def get_itemsprice_only(self):
        onlyitemsprice = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_itemsprice_xpath))).text
        return int(float(onlyitemsprice.replace("₹", "").replace(",", "")))

    def get_delivery_address(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, self.text_deliveryaddress_id))).text

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
        return Addressline1

    ##############
    def verify_checkout_page(self):
        return self.wait.until(EC.title_is("Place Your Order - Amazon Checkout"))

    def get_item_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_itemprice_xpath))).text

    def get_delivery_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_deliveryprice_xpath))).text

    def get_pay_on_delivery_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_payondeliveryfee_xpath))).text

    def get_item_total(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_itemtotal_xpath))).text

    def get_free_delivery_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_freedelivery_xpath))).text

    def get_order_total(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_ordertotal_xpath))).text

    def click_on_change_address(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.alink_changeaddress_xpath))).click()

    def click_on_show_more_addresses(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_showmoreaddress_xpath))).click()

    def click_on_an_existing_address(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_2ndaddress_xpath))).click()

    #Add New Address
    def click_on_add_new_address(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_addnewaddress_xpath))).click()

    def select_country_from_dropdown(self, country):
        countrydd = self.wait.until(EC.visibility_of_element_located((By.ID, self.dropdown_country_id)))
        s = Select(countrydd)
        s.select_by_visible_text(country)

    def enter_full_name(self, name):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_fullname_id))).send_keys(name)

    def enter_mobile_number(self, mobilenumber):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_mobilenumber_id))).send_keys(mobilenumber)

    def enter_pin_code(self, pincode):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_pincode_id))).send_keys(pincode)

    def enter_address_line_1(self, addressline1):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_addressline1_id))).send_keys(addressline1)

    def enter_address_line_2(self, addressline2):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_addressline2_id))).send_keys(addressline2)

    def enter_landmark(self, landmark):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_landmark_id))).send_keys(landmark)

    def enter_city(self, city):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.text_city_id))).send_keys(city)

    def select_state_from_dropdown(self, state):
        statedd=self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_state_xpath)))
        s=Select(statedd)
        s.select_by_visible_text(state)

    def click_on_make_this_my_default_address_checkbox(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.checkbox_makethismydefaultaddress_id))).click()

    def click_on_delivery_instructions(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.alink_deliveryinstructions_xpath))).click()

    def click_on_address_type_HOME(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addresstypeHOME_xpath))).click()

    def click_on_address_type_APARTMENT(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addresstypeAPARTMENT_xpath))).click()

    def click_on_address_type_BUSINESS(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addresstypeBUSINESS_xpath))).click()

    def click_on_address_type_OTHER(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_addresstypeOTHER_xpath))).click()

    def click_on_weekened_confirmation(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.accordion_weekenedconfirmation_xpath))).click()

    def click_on_saturday_NO(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_saturdayNO_xpath))).click()

    def click_on_saturday_YES(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_saturdayYES_xpath))).click()

    def click_on_sunday_NO(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_sundayNO_xpath))).click()

    def click_on_sunday_YES(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_saturdayYES_xpath))).click()

    def click_on_additional_instructions(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.accordion_additionalinstructions_xpath))).click()

    def enter_delivery_instructions(self, deliveryinstructions):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.textarea_deliveryinstruction_id))).send_keys(deliveryinstructions)

    def click_on_use_this_address(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_usethisaddress_xpath))).click()

    def click_on_deliver_to_this_address(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.button_delivertothisaddress_id))).click()


    #error messages for mandatory address fields unfilled
    def get_error_message_for_full_name(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_errorname_xpath), "Please enter a name."))

    def get_error_message_for_mobile_number(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_mobile_xpath), "Please enter a phone number so we can call if there are any issues with delivery."))

    def get_error_message_for_pincode(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_pincode_xpath), "Please enter a ZIP or postal code."))

    def get_error_message_for_address_line(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_addressline1_xpath), "Please enter an address."))

    def get_error_message_for_city(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_city_xpath),"Please enter a city name."))

    def get_error_message_for_state(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.text_state_xpath), "Please enter a state, region or province."))

    #change payment method
    def click_on_change_payment_method(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.alink_changepaymentmethod_xpath))).click()

    #credit card
    def click_on_credit_card(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_card_xpath))).click()

    def click_on_add_card_details(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.alink_addcarddetails_xpath))).click()

    # def CardNumber(self, cardnumber):
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, self.textarea_cardnumber_xpath))).send_keys(cardnumber)
    # 
    # def Nickname(self, nickname):
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textarea_nickname_name))).send_keys(nickname)
    # 
    # def ExpiryMonth(self, month):
    #     monthdd=self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_expiryMonth_xpath)))
    #     s=Select(monthdd)
    #     s.select_by_visible_text(month)
    # 
    # def ExpiryYear(self, year):
    #     yeardd=self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dropdown_expiryYear_xpath)))
    #     s=Select(yeardd)
    #     s.select_by_visible_text(year)
    # 
    # def ContinueCard(self):
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_cardContinue_xpath))).click()
    # 
    # def CancelCard(self):
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_cartCancel_xpath))).click()

    #net banking
    def click_on_net_banking(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.radio_netbanking_xpath))).click()


    def click_on_increase_quantity(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.button_incrementquantity_xpath))).click()

    def click_on_decrease_quantity(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.button_decrementquantity_xpath))).click()

    #Back to cart
    def click_on_back_to_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.alink_backtocart_xpath))).click()

    #Place order
    def verify_if_place_oder_button_is_enabled(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_placeorder_xpath))).is_enabled()

