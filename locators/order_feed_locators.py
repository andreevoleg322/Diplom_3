from selenium.webdriver.common.by import By

class OrderLocators:

    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]') #кнопка "Лента заказов"
    ORDER_IN_FEED = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') #заказ из списка
    ORDER_INFO = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5") #окно с заказом
    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') #ингредиент Флюоресцентная булка
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') #область создания бургера
    EMAIL = (By.XPATH, '//input[@name="name"]') #поле "Email" в форме входа
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]') #поле "Пароль" в форме входа
    SUBMIT_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') #кнопка "Оформить заказ"
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') #кнопка "Войти в аккаунт"
    ORDER_CREATE_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') #кнопка оформления заказа
    ORDER_EXIT_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK") #кнопка закрытия оформления заказа
    PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]') #кнопка "Личный кабинет"
    ORDER_HISTORY = (By.XPATH, '//a[contains(text(),"История заказов")]')  #кнопка "Итория заказов"
    HISTORY_ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']") #номер заказа в истории заказов
    FEED_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]") #номер заказа в ленте заказов
    ORDER_ALL_TIME = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]") #выполнено за все время
    ORDER_TODAY = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]") #выполнено за сегодня
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') #кнопка "Конструктор"
    ORDER_NUMBER = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]") #номер заказа в окне после оформления
    ORDER_NUMBER_WORK = (By.XPATH,"//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]") #номер заказа в окне после оформления