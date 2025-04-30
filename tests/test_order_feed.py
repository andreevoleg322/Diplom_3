from pages.order_feed_page import OrderFeed
from conftest import driver
import allure
import time

class TestOrderFeed:

    @allure.description("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_open_details(self, driver):
        order_feed = OrderFeed(driver)

        order_feed.wait_order_feed()
        order_feed.click_order_feed()

        order_feed.click_order_in_feed()
        time.sleep(5)
        assert order_feed.check_displaying_order_info()

    @allure.description("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_history_order_in_feed_oder(self, driver, test_user):
        order_feed = OrderFeed(driver)

        order_feed.wait_order_feed()
        order_feed.login_to_account(test_user)

        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_order_create_button()
        order_feed.click_order_exit_button()

        order_feed.click_order_personal_account()
        order_feed.click_history_order()
        order_number_history = order_feed.text_history_order_number()
        order_feed.click_order_feed()
        order_number_feed = order_feed.text_feed_order_number()
        assert order_number_feed in order_number_history

    @allure.description("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_counter_all_time(self, driver, test_user):
        order_feed = OrderFeed(driver)

        order_feed.wait_order_feed()
        order_feed.login_to_account(test_user)

        order_feed.click_order_feed()
        order_all_time = int(order_feed.text_order_all_time())

        order_feed.click_constractor()

        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_order_create_button()
        order_feed.click_order_exit_button()

        order_feed.click_order_feed()
        order_all_time_after = int(order_feed.text_order_all_time())
        assert order_all_time + 1 == order_all_time_after

    @allure.description("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_counter_order_today(self, driver, test_user):
        order_feed = OrderFeed(driver)

        order_feed.wait_order_feed()
        order_feed.login_to_account(test_user)

        order_feed.click_order_feed()
        order_today = int(order_feed.text_order_today())

        order_feed.click_constractor()

        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_order_create_button()
        order_feed.click_order_exit_button()

        order_feed.click_order_feed()
        order_today_after = int(order_feed.text_order_today())
        assert order_today + 1 == order_today_after

    @allure.description("После оформления заказа его номер появляется в разделе В работе")
    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_work(self, driver, test_user):
        order_feed = OrderFeed(driver)

        order_feed.wait_order_feed()
        order_feed.login_to_account(test_user)

        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_order_create_button()
        order_number = order_feed.text_order_number()
        order_feed.click_order_exit_button()

        order_feed.click_order_feed()
        assert order_feed.wait_order_appears_in_progress(order_number), "Заказ не появился"
        order_number_work = order_feed.text_order_number_work()
        assert order_number in order_number_work