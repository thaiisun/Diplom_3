import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic('UI Stellar Burgers')
@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Счётчик «Выполнено за все время» увеличивается после заказа')
    def test_total_counter_increases_after_order(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.login(test_user['email'], test_user['password'])
        order_feed_page.open_order_feed_page()
        counter_before = order_feed_page.get_total_counter()

        main_page.open_main_page()
        main_page.drag_first_ingredient_to_basket()
        main_page.click_place_order()
        main_page.get_order_number()

        order_feed_page.open_order_feed_page()
        counter_after = order_feed_page.wait_total_counter_changed(counter_before)

        with allure.step('Проверяем, что счётчик увеличился'):
            assert int(counter_after) > int(counter_before)

    @allure.title('Счётчик «Выполнено за сегодня» увеличивается после заказа')
    def test_today_counter_increases_after_order(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.login(test_user['email'], test_user['password'])
        order_feed_page.open_order_feed_page()
        counter_before = order_feed_page.get_today_counter()

        main_page.open_main_page()
        main_page.drag_first_ingredient_to_basket()
        main_page.click_place_order()
        main_page.get_order_number()

        order_feed_page.open_order_feed_page()
        counter_after = order_feed_page.wait_today_counter_changed(counter_before)

        with allure.step('Проверяем, что счётчик увеличился'):
            assert int(counter_after) > int(counter_before)

    @allure.title('Номер оформленного заказа появляется в разделе «В работе»')
    def test_new_order_appears_in_progress(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.login(test_user['email'], test_user['password'])
        main_page.open_main_page()
        main_page.drag_first_ingredient_to_basket()
        main_page.click_place_order()
        order_number = main_page.get_order_number()

        order_feed_page.open_order_feed_page()

        with allure.step('Проверяем, что номер заказа появился в разделе «В работе»'):
            assert order_feed_page.wait_order_in_progress(order_number)