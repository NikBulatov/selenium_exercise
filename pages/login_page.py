from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registered_form()

    def should_be_login_url(self):
        assert self.url == self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_registered_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registered form is not presented"

    def register_new_user(self, email: str, password: str):
        if isinstance(email, str) and isinstance(password, str):
            self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTER_1PASSWORD_FIELD).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_2PASSWORD_FIELD).send_keys(password)

            self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()
        else:
            raise ValueError('email and password arguments should be "str" type')

    def should_be_success_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS_MESSAGE), 'User was not registered'

