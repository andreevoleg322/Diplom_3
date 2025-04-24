from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visibility_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        element = self.wait_clickable_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_visibility_element(locator)
        element.send_keys(text)

    def get_text_element(self, locator):
        element = self.wait_visibility_element(locator)
        return element.text

    def check_displaying_element(self, locator):
        try:
            return self.wait_visibility_element(locator).is_displayed()
        except:
            return False

    def check_text_element(self, locator, expected_text):
        actual_text = self.get_text_element(locator)
        return actual_text == expected_text

    def get_url(self):
        return self.driver.current_url

    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()