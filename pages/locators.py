from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BACKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")#кнопка добавить в корзину
    PRICE_ITEM  = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color") #цена товара
    ITEM_IN_BACKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") #товар в корзине
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child")   #название товара
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong") #цена товара в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")
   