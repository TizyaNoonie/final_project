import faker
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import BasketPageLocators, LoginPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LoginPageLocators.LINK)
        page.open()
        page.register_new_user(faker.Faker().email(), faker.Faker().password())
        page.should_be_authorized_user()

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, BasketPageLocators.LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, BasketPageLocators.LINK)
        page.open()
        page.should_add_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_add_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_text()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
@pytest.mark.xfail(reason="This test should fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail(reason="This test should fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_add_to_basket()
    page.should_disappear_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, BasketPageLocators.LINK)
    page.open()
    page.should_be_login_link()
