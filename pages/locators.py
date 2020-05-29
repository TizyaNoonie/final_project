from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators(object):
    LOGIN_FORM = By.CSS_SELECTOR, "#login_form"
    REGISTER_FORM = By.CSS_SELECTOR, "#register_form"


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, ".btn.btn-add-to-basket"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, ".alert-safe"
    PRODUCT_ADDED = By.CSS_SELECTOR, ".alert-success:first-child strong"
    PRODUCT_CHOSEN = By.CSS_SELECTOR, ".product_main h1"
    BASKET_PRICE = By.CSS_SELECTOR, ".alert-info strong"
    PRODUCT_PRICE = By.CSS_SELECTOR, ".product_page .product_main p.price_color"
