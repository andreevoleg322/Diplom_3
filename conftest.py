import pytest
from urls import Url
from webdriver_factory import WebDriverFactory
from faker import Faker
import requests

fake = Faker()


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    browser_name = request.param
    driver = WebDriverFactory.get_driver(browser_name)
    driver.get(Url.URL_LOGIN)

    yield driver

    driver.quit()

@pytest.fixture
def test_email():

    return fake.email()

@pytest.fixture(scope="function")
def test_user():
    test_user_data = {
        "email": fake.email(),
        "password": "password",
        "name": fake.name()
    }

    response = requests.post(Url.USER_REGISTER, json=test_user_data)
    response_body = response.json()

    yield {
        "email": test_user_data["email"],
        "password": test_user_data["password"],
        "name": test_user_data["name"]
    }

    access_token = response_body.get('accessToken')
    if access_token:
        requests.delete(Url.USER_DELETE, headers={'Authorization': access_token})