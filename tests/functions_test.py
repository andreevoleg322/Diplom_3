from pages.functions_page import FunctionsPage
from conftest import driver
import allure
from urls import Url

class TestFunctions:

    @allure.description("Переход по клику на «Конструктор»")
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_button_constructor(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()
        assert function.check_url() == Url.url_constructor

    @allure.description("Переход по клику на «Лента заказов»")
    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_order_feed()
        assert function.check_displaying_title_feed_order()

    @allure.description("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.click_ingredient()
        assert function.check_ingredient()

    @allure.description("Всплывающее окно закрывается кликом по крестику")
    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_closed(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.click_ingredient()
        function.wait_closed()
        function.click_closed()
        assert function.check_closed

    @allure.description("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_add_ingredient_and_count_increment(self, driver):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.click_button_constructor()

        function.wait_bun()
        function.drag_and_drop_ingredient_to_burger_area()
        assert function.get_count_of_ingredients() == '2'

    @allure.description("Залогиненный пользователь может оформить заказ")
    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_login_user(self, driver, test_user):
        function = FunctionsPage(driver)

        function.wait_button_constructor()
        function.login_to_account(test_user)

        function.wait_bun()
        function.drag_and_drop_ingredient_to_burger_area()
        function.click_order()
        assert function.check_order