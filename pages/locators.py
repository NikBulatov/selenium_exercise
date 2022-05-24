from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    USER_ICON = (By.CLASS_NAME, 'icon-user')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FIELD = (By.NAME, 'registration-email')
    REGISTER_1PASSWORD_FIELD = (By.NAME, 'registration-password1')
    REGISTER_2PASSWORD_FIELD = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.NAME, 'registration_submit')
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')


class MainPageLocators(BasePageLocators):
    pass


class ProductPageLocators(BasePageLocators):
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_ITEM = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    ITEM = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_CASH = (By.CLASS_NAME, 'hidden-xs')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasketPageLocators(BasePageLocators):
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_SET = (By.ID, 'basket_formset')
