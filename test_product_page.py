from time import time
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email, password = str(time()) + '@nik.ki', 'Test!12345'
        login_page = LoginPage(browser, LoginPage.LINK)
        login_page.open()
        login_page.should_be_registered_form()
        login_page.register_new_user(email, password)
        login_page.should_be_success_message()
        login_page.should_be_authorized_user()
        print(f'New user was registered and authorized: email - {email}, password - {password}')

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
        product_page.open()
        product_page.should_be_add_button()
        product_page.add_to_basket_button()
        # product_page.solve_quiz_and_get_code()
        product_page.item_should_be_added_correctly()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
        product_page.open()
        product_page.should_be_add_button()
        product_page.add_to_basket_button()
        product_page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
        product_page.open()
        product_page.should_be_add_button()
        product_page.add_to_basket_button()
        product_page.not_should_be_success_message()


@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, index):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{index}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_button()
    product_page.add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.item_should_be_added_correctly()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, TestUserAddToBasketFromProductPage.LINK)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket_page()
    product_page = BasketPage(browser, browser.current_url)
    product_page.should_be_empty_basket()
    product_page.should_be_empty_basket_message()
