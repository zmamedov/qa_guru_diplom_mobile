import os

from appium.options.android import UiAutomator2Options
from qa_guru_diplom_mobile.utils.path import abs_path_from_project

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')


def to_driver_options():
    options = UiAutomator2Options()

    options.set_capability('platformName', os.getenv('platformName', 'android'))
    options.set_capability('deviceName', os.getenv('deviceName', 'emulator-5554'))
    options.set_capability('appWaitActivity', os.getenv('appWaitActivity', 'org.wikipedia.*'))
    options.set_capability('app', os.getenv('app', abs_path_from_project('app-alpha-universal-release.apk')))

    return options
