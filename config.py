import os
import pydantic
from appium.options.android import UiAutomator2Options
from qa_guru_diplom_mobile.utils.path import abs_path_from_project

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')


class Config(pydantic.BaseSettings):
    remote_url: str = 'http://127.0.0.1:4723'
    platformName: str = 'android'
    deviceName: str = 'emulator-5554'
    appWaitActivity: str = 'org.wikipedia.*'
    app: str = abs_path_from_project('app-alpha-universal-release.apk')


config = Config()


def to_driver_options():
    options = UiAutomator2Options()

    options.set_capability('platformName', config.platformName)
    options.set_capability('deviceName', config.deviceName)
    options.set_capability('appWaitActivity', config.appWaitActivity)
    options.set_capability('app', config.app)

    return options
