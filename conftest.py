import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_helpers import generate_user_data, register_user_via_api, delete_user_via_api


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture
def test_user():
    user_data = generate_user_data()
    access_token = register_user_via_api(user_data)

    yield user_data

    if access_token:
        delete_user_via_api(access_token)