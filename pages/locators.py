from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class MainPageLocators(BasePageLocators):
    pass


class ProductPageLocators(BasePageLocators):
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_ITEM = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    ITEM = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_CASH = (By.CLASS_NAME, 'hidden-xs')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
