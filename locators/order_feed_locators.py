from selenium.webdriver.common.by import By


class OrderFeedLocators:
    TOTAL_LABEL = (By.XPATH, "//p[text()='Выполнено за все время:']")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    TODAY_LABEL = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]")
    TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")

    IN_PROGRESS_LABEL = (By.XPATH, "//p[text()='В работе:']")
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")