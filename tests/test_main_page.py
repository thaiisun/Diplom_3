import allure

from data import Texts
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic('UI Stellar Burgers')
@allure.feature('Основная функциональность')
class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_opens_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_order_feed()
        main_page.click_constructor()

        with allure.step('Проверяем, что открылся конструктор'):
            assert main_page.is_constructor_displayed()

    @allure.title('Переход по клику на «Лента Заказов»')
    def test_click_order_feed_opens_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.open_main_page()

        main_page.click_order_feed()

        with allure.step('Проверяем, что открылась лента заказов'):
            assert order_feed_page.is_order_feed_displayed()

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_first_ingredient()

        with allure.step('Проверяем, что появилось окно с деталями'):
            assert main_page.is_ingredient_modal_displayed()

    @allure.title('Окно с деталями ингредиента закрывается по клику на крестик')
    def test_close_ingredient_modal_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()

        with allure.step('Проверяем, что окно закрылось'):
            main_page.wait_ingredient_modal_closed()
            assert not main_page.is_ingredient_modal_displayed()

    @allure.title('При добавлении ингредиента счётчик увеличивается')
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        counter_before = main_page.get_first_ingredient_counter()
        main_page.drag_first_ingredient_to_basket()
        counter_after = main_page.wait_counter_changed(counter_before)

        with allure.step('Проверяем, что счётчик увеличился'):
            assert int(counter_after) > int(counter_before or 0)