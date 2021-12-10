from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators



class ProductPage(BasePage): 
    def guest_can_add_product_to_basket(self): #добавить в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_BACKET_BUTTON)
        button.click()

    def should_be_item_in_basket(self):         #проверка что товар добавлен в корзину
        item_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_IN_BACKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert item_in_basket.text == product_name_in_store.text, "товар не лежит в корзине"
        print("Товар добавлен в корзину")

    def should_basket_price(self):       #проверка что цена добавлена в корзину
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM)
        price_item_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_ITEM)
        assert price_item.text == price_item_in_basket.text, "цена не совпадает"
        print("Цена товара", price_item_in_basket.text)


        
    def check_message_about_adding_to_basket(self):
        basket_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе отображается, но не должно"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Сообщение об успехе отображается, но не должно"

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе не исчезло"
        