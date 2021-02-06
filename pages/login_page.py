from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'В ссылке отсутствует "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина не найдена'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации не найдена'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_input2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
