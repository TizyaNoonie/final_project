from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import WebDriverException


class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()
        self.should_be_clickable_button()
        self.solve_quiz_and_get_code()
        self.should_be_success_add_message()
        self.should_product_chosen_equal_product_added()
        self.should_be_equal_product_and_basket_prices()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert "catalogue" in current_url, f"There is no 'catalogue' in current url, which is '{current_url}'"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "There is no 'add to basket' button"

    def should_be_clickable_button(self):
        try:
            btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
            btn.click()
        except WebDriverException:
            assert False, "Cannot find or click 'add to cart' button"

    def should_be_success_add_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "There is no success message after adding to cart"

    def should_product_chosen_equal_product_added(self):
        product_chosen = self.browser.find_element(*ProductPageLocators.PRODUCT_CHOSEN).text
        product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        assert product_added == product_chosen, f"'{product_chosen}' should equal '{product_added}' added to basket"

    def should_be_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE)

    def should_be_equal_product_and_basket_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"'{product_price}' should be equal to '{basket_price}'"

    def should_not_disappear_success_message(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message has disappeared, but should be'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message has not disappeared, but should be'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



