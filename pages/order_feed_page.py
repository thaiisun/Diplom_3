import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from urls import Urls


class OrderFeedPage(BasePage):

    @allure.step('Открыть страницу «Лента Заказов»')
    def open_order_feed_page(self):
        self.open_page(Urls.ORDER_FEED_PAGE)

    @allure.step('Проверить, что открыта лента заказов')
    def is_order_feed_displayed(self):
        return self.is_element_displayed(OrderFeedLocators.TOTAL_LABEL)

    @allure.step('Получить счётчик «Выполнено за все время»')
    def get_total_counter(self):
        return self.get_element_text(OrderFeedLocators.TOTAL_COUNTER)

    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_today_counter(self):
        return self.get_element_text(OrderFeedLocators.TODAY_COUNTER)

    @allure.step('Дождаться увеличения счётчика «Выполнено за все время»')
    def wait_total_counter_changed(self, old_value):
        return self.wait_for_text_change(OrderFeedLocators.TOTAL_COUNTER, old_value)

    @allure.step('Дождаться увеличения счётчика «Выполнено за сегодня»')
    def wait_today_counter_changed(self, old_value):
        return self.wait_for_text_change(OrderFeedLocators.TODAY_COUNTER, old_value)

    @allure.step('Получить список номеров заказов из раздела «В работе»')
    def get_in_progress_order_numbers(self):
        try:
            elements = self.driver.find_elements(*OrderFeedLocators.IN_PROGRESS_ORDERS)
            numbers = []
            for element in elements:
                text = element.text.strip().lstrip('#')
                if text.isdigit():
                    numbers.append(str(int(text)))
            return numbers
        except StaleElementReferenceException:
            return []

    @allure.step('Дождаться появления номера заказа в разделе «В работе»')
    def wait_order_in_progress(self, order_number):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            lambda driver: order_number in self.get_in_progress_order_numbers()
        )
        return True