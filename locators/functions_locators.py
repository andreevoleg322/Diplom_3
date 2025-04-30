from selenium.webdriver.common.by import By

class FunctionsLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') #кнопка "Конструктор"
    FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]') #кнопка "Лента заказов"
    TITLE_FEED_ORDER = (By.XPATH, '//h1[contains(text(),"Лента заказов")]') #заголовок Лента заказов
    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') #ингредиент Флюоресцентная булка
    INGREDIENT_BUN_INFO = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]') #информация карточки Флюоресцентная булка
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')  #область создания бургера
    COUNT_INGREDIENT = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')  #значение булки
    INGREDIENT_CLOSE = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified__3V5XS")]') #кнопка закрытия окна ингредиента
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')  #кнопка "Войти в аккаунт"
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  #поле "Пароль" в форме входа
    EMAIL = (By.XPATH, '//input[@name="name"]')  #поле "Email" в форме входа
    SUBMIT_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')  #кнопка "Оформить заказ"
    STARTING_ORDER = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]') #надпись "Ваш заказ начали готовить"















