from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        current_url = self.browser.current_url
        assert "basket" in current_url, f"There is no 'basket' in current url, which is '{current_url}'"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are items in basket, though should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "There is no 'basket is empty' text, though should be"
