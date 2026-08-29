import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls

DRAG_AND_DROP_SCRIPT = """
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();

const dragStart = new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer});
source.dispatchEvent(dragStart);

const dragOver = new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer});
target.dispatchEvent(dragOver);

const drop = new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer});
target.dispatchEvent(drop);

const dragEnd = new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer});
source.dispatchEvent(dragEnd);
"""


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_page(Urls.BASE_URL)

    @allure.step('Кликнуть на «Конструктор»')
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на «Лента Заказов»')
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на «Личный Кабинет»')
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть на «Войти в аккаунт»')
    def click_login_account(self):
        self.click_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Проверить, что открыт конструктор')
    def is_constructor_displayed(self):
        return self.is_element_displayed(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Кликнуть на первый ингредиент')
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Проверить, что открыто окно с деталями ингредиента')
    def is_ingredient_modal_displayed(self):
        return self.is_element_displayed(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Закрыть окно с деталями ингредиента')
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step('Дождаться закрытия окна с деталями ингредиента')
    def wait_ingredient_modal_closed(self):
        self.wait_for_element_disappear(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Получить значение счётчика первого ингредиента')
    def get_first_ingredient_counter(self):
        return self.get_element_text(MainPageLocators.FIRST_INGREDIENT_COUNTER)

    @allure.step('Перетащить первый ингредиент в конструктор')
    def drag_first_ingredient_to_basket(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.CONSTRUCTOR_BASKET,
            DRAG_AND_DROP_SCRIPT
        )

    @allure.step('Дождаться увеличения счётчика первого ингредиента')
    def wait_counter_changed(self, old_value):
        return self.wait_for_text_change(
            MainPageLocators.FIRST_INGREDIENT_COUNTER, old_value
        )

    @allure.step('Нажать «Оформить заказ»')
    def click_place_order(self):
        self.click_element_js(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получить номер оформленного заказа')
    def get_order_number(self):
        self.wait_for_element(MainPageLocators.ORDER_MODAL_TEXT)
        number = self.wait_for_text_change(MainPageLocators.ORDER_NUMBER, '9999')
        return str(int(number.strip().lstrip('#')))