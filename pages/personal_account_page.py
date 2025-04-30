from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):

    @allure.step("Вход в личный кабинет")
    def login_to_account(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        self.enter_text(PersonalAccountLocators.EMAIL, email)
        self.enter_text(PersonalAccountLocators.PASSWORD_NAME, password)
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON)


    @allure.step("Ожидание кнопки «Войти»")
    def wait_button_account(self):
        self.wait_clickable_element(PersonalAccountLocators.LOGIN_BUTTON)

    @allure.step("Клик по кнопке «Войти»")
    def click_button_account(self):
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON)

    @allure.step("Ожидание кнопки «Личный кабинет»")
    def wait_button_personal_account(self):
        self.wait_clickable_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке «Личный кабинет»")
    def click_button_personal_account(self):
        self.click_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Ожидание кнопки «История заказов»")
    def wait_history_order(self):
        self.wait_clickable_element(PersonalAccountLocators.HISTORY_ORDER)

    @allure.step("Клик кнопки «История заказов»")
    def click_history_order(self):
        self.click_element(PersonalAccountLocators.HISTORY_ORDER)

    @allure.step("Клик кнопки «Выход»")
    def click_exit(self):
        self.click_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step("Получить ссылку текущей страницы")
    def check_url(self):
        return self.get_url()