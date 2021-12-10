from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason="Исправить баг")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_item_in_basket()
    page.should_basket_price()
    page.check_message_about_adding_to_basket()
