import os

import pydantic_settings
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from telegram_mobile_test_project.utils.path import abs_path_from_project


class Config(pydantic_settings.BaseSettings):
    remote_url: str = os.getenv('REMOTE_URL')
    platform_name: str = os.getenv('PLATFORM_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION', '9.0')
    device_name: str = os.getenv('DEVICE_NAME')
    load_dotenv(dotenv_path=abs_path_from_project('.env.credentials'))
    login: str = os.getenv('LOGIN')
    accessKey: str = os.getenv('ACCESS_KEY')
    app: str = os.getenv('APP')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('app', abs_path_from_project(self.app))
        elif context == 'local_device':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('app', abs_path_from_project(self.app))
        elif context == 'browserstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformName', self.platform_version)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Mobile test project',
                    'buildName': 'app-build-1',
                    'sessionName': 'Browserstack tests',
                    'userName': self.login,
                    'accessKey': self.accessKey,
                },
            )

        return options


config_object = Config()
