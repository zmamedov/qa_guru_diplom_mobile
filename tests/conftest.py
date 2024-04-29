import pytest
from appium import webdriver
from selene import browser

from config import config_object


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config_object.to_driver_options()
    browser.config.driver = webdriver.Remote(command_executor=config_object.remote_url, options=options)

    yield

    browser.quit()
