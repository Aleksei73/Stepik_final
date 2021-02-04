from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_NAME)[0].text == \
               self.browser.find_element(*ProductPageLocators.BOOK_NAME).text,\
               'После добавления в корзину не совпадают именна '
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BASKET_NOW).text,\
               'Не совпадают цены после добавления в корзину '
