from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') #кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') #кнопка "Войти в аккаунт"
    EMAIL = (By.XPATH, '//input[@name="name"]') #поле "Email" на форме входа
    PASSWORD_NAME = (By.XPATH, '//input[@name="Пароль"]') #поле "Пароль" в форме входа
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]') #кнопка "История заказов"
    EXIT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]') #кнопка "Выход"
    ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')  #кнопка "Оформить заказ"