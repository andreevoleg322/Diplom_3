from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:

    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]') #кнопка восстановления пароля
    RECOVERY_PASSWORD_EMAIL = (By.CLASS_NAME, 'input__textfield') #поле ввода Email
    RECOVERY_BUTTON = (By.XPATH, '//button[contains(text(),"Восстановить")]') #кнопка "Восстановить" в форме восстановления пароля
    SAVE_RECOVERY_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]') #кнопка "Сохранить" в форме восстановления пароля
    HIDE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #иконка открытия/скрытия пароля
    ACTIVE_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]') #активное поле ввода пароля