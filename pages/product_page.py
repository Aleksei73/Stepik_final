from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_right_name_and_price(self):
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_NAME)[0].text == \
               self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, \
            'После добавления в корзину не совпадают именна '
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BASKET_NOW).text, \
            'Не совпадают цены после добавления в корзину '

    def should_cant_see_seccess_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Cообщение есть'

    def should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Cообщение не пропало'
