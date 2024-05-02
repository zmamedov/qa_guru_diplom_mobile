import os
import allure
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

from telegram_mobile_test_project.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--context',
        default='emulator',
        help='Specify the test context'
    )


@pytest.fixture
def context(request):
    return request.config.getoption('--context')


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    env_file_path = f'.env.{context}'
    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f'Warning: Configuration file "{env_file_path}" not found.')

    from config import config_object

    options = config_object.to_driver_options(context)

    with allure.step('Setup app session'):
        browser.config.driver = webdriver.Remote(command_executor=config_object.remote_url, options=options)

    yield

    attach.add_screenshot()
    attach.add_xml()
    session_id = browser.driver.session_id

    with allure.step('Tear down app session with id' + session_id):
        browser.quit()

    if context == 'browserstack':
        attach.add_video(session_id)
