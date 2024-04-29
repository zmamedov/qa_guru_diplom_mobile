import os
import pydantic_settings
from appium.options.android import UiAutomator2Options
from qa_guru_diplom_mobile.utils.path import abs_path_from_project

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')


class Config(pydantic_settings.BaseSettings):
    context: str = 'emulator'
    remote_url: str = 'http://127.0.0.1:4723'
    platformName: str = 'Android'
    platformVersion: str = '9.0'
    deviceName: str = 'emulator-5554'
    appWaitActivity: str = 'org.wikipedia.*'
    projectName: str = 'First Python project'
    buildName: str = 'browserstack-build-1'
    sessionName: str = 'BStack first_test'
    userName: str = 'login'
    accessKey: str = 'accessKey'
    app: str = abs_path_from_project('app-alpha-universal-release.apk')

    def to_driver_options(self):
        options = UiAutomator2Options()

        if self.context == 'emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platformName)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app)
        elif self.context == 'local_device':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platformName)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app)
        elif self.context == 'browserstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformName', self.platformVersion)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('projectName', self.projectName)
            options.set_capability('buildName', self.buildName)
            options.set_capability('sessionName', self.sessionName)
            options.set_capability('userName', self.userName)
            options.set_capability('accessKey', self.accessKey)
            options.set_capability('app', self.app)

        return options


config_object = Config()
