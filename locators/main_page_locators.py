from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient')])[1]")
    FIRST_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//a[contains(@class,'BurgerIngredient')])[1]//p[contains(@class,'counter_counter__num')]"
    )

    INGREDIENT_MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']/following::button[contains(@class,'Modal_modal__close')][1]"
    )

    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    ORDER_MODAL_TEXT = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]") 