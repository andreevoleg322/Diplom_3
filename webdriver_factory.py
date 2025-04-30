from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):

        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается.")