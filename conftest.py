import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


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