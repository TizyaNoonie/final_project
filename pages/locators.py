from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, "#login_link_inc"
    BASKET_LINK = By.CSS_SELECTOR, ".btn.btn-default[href*='/basket/']:first-child"
    USER_ICON = By.CSS_SELECTOR, ".icon-user"


class BasketPageLocators(object):
    BASKET_ITEMS = By.CSS_SELECTOR, ".basket-items"
    EMPTY_BASKET_TEXT = By.CSS_SELECTOR, "#content_inner > p"
    LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class LoginPageLocators(object):
    LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = By.CSS_SELECTOR, "#login_form"
    REGISTER_FORM = By.CSS_SELECTOR, "#register_form"

    REGISTER_EMAIL = By.CSS_SELECTOR, "#id_registration-email"
    REGISTER_PASSWORD1 = By.CSS_SELECTOR, "#id_registration-password1"
    REGISTER_PASSWORD2 = By.CSS_SELECTOR, "#id_registration-password2"
    REGISTER_BTN = By.CSS_SELECTOR, "[name='registration_submit']"

    LOGIN_EMAIL = By.CSS_SELECTOR, "#id_login-username"
    LOGIN_PASSWORD = By.CSS_SELECTOR, "#id_login-password"
    LOGIN_BTN = By.CSS_SELECTOR, "[name='login_submit']"


class MainPageLocators(object):
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, ".btn.btn-add-to-basket"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, ".alert-safe"
    PRODUCT_ADDED = By.CSS_SELECTOR, ".alert-success:first-child strong"
    PRODUCT_CHOSEN = By.CSS_SELECTOR, ".product_main h1"
    BASKET_PRICE = By.CSS_SELECTOR, ".alert-info strong"
    PRODUCT_PRICE = By.CSS_SELECTOR, ".product_page .product_main p.price_color"
