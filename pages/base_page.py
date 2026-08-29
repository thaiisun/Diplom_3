import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Дождаться появления элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.wait_for_clickable(locator).click()

    @allure.step('Кликнуть по элементу через JavaScript')
    def click_element_js(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Ввести текст в поле')
    def fill_field(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    @allure.step('Получить тексты всех найденных элементов')
    def get_elements_texts(self, locator):
        try:
            return [element.text for element in self.driver.find_elements(*locator)]
        except StaleElementReferenceException:
            return []

    @allure.step('Проверить, что элемент отображается')
    def is_element_displayed(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except Exception:
            return False

    @allure.step('Дождаться исчезновения элемента')
    def wait_for_element_disappear(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Дождаться изменения текста элемента')
    def wait_for_text_change(self, locator, old_text):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            lambda driver: driver.find_element(*locator).text != old_text
        )
        return self.get_element_text(locator)

    @allure.step('Дождаться выполнения условия')
    def wait_for_condition(self, condition):
        WebDriverWait(self.driver, self.TIMEOUT).until(lambda driver: condition())
        return True

    @allure.step('Перетащить элемент в целевую область')
    def drag_and_drop(self, source_locator, target_locator, script):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        self.driver.execute_script(script, source, target)

    @allure.step('Прокрутить к элементу')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
        return element