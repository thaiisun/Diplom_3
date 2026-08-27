import allure

from data import UserData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):

    @allure.step('Открыть страницу входа')
    def open_login_page(self):
        self.open_page(Urls.LOGIN_PAGE)

    @allure.step('Ввести email')
    def fill_email(self, email):
        self.fill_field(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Ввести пароль')
    def fill_password(self, password):
        self.fill_field(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Нажать кнопку «Войти»')
    def click_login_button(self):
        self.click_element_js(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Дождаться завершения авторизации')
    def wait_for_login_complete(self):
        self.wait_for_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Войти в аккаунт')
    def login(self, email=UserData.EMAIL, password=UserData.PASSWORD):
        self.open_login_page()
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()
        self.wait_for_login_complete()