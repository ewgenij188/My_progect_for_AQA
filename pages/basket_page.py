from types import BuiltinFunctionType
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_LINK) #жмем на корзину
        button.click()

    def guest_see_empty_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Корзина не пуста, а должна быть"

    def guest_see_not_item_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Товар есть в корзине, но не должен"