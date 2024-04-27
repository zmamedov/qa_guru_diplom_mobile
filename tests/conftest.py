import pytest
from appium import webdriver
from selene import browser

import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config.to_driver_options()
    browser.config.driver = webdriver.Remote(command_executor=config.remote_url, options=options)

    yield

    browser.quit()
