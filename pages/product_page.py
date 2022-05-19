from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Add to basket button is not presented'

    def add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def item_should_be_added(self):
        added_item_text = self.browser.find_element(*ProductPageLocators.ADDED_ITEM).text
        assert self.get_item_name() == added_item_text, 'Item is not added to basket'

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM).text

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def item_price_should_be_equal(self):
        price = self.browser.find_element(*ProductPageLocators.BASKET_CASH).text.split('\n')[0].split()[-1]
        assert self.get_item_price() == price, 'Price does not match'

    def item_should_be_added_correctly(self):
        self.item_should_be_added()
        self.item_price_should_be_equal()
