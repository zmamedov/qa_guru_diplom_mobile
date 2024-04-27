import pytest
from appium import webdriver
from selene import browser
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'deviceName': 'emulator-5554',
        'appWaitActivity': 'org.wikipedia.*',
        'app': 'XXXXXXXXXX',
    })

    browser.config.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    yield

    browser.quit()

